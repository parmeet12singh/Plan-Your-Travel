from neo4j import GraphDatabase
from . import get_coordinates
import os

class Database:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_airlines_destinations(self, source, airlinesWithDestinations):

        with self.driver.session() as session:
            session.write_transaction(self._create_city, source)

            for i in airlinesWithDestinations:
                
                airline = i[0]
                session.write_transaction(self._create_airline, airline)

                destinations = i[1]
                for destination in destinations:
                    
                    if(destination.find('–')!=-1):
                        destination = destination[0:destination.find('–')]
                    if(destination.find('-')!=-1):
                        destination = destination[0:destination.find('-')]
                    if(destination.find('City')!=-1):
                        destination = destination.replace('City', ' City')
                    
                    session.write_transaction(self._create_city, destination)
                    session.write_transaction(self._create_has_direct_flight_relationship, source, destination)
                
                session.write_transaction(self._create_has_operations_in, airline, source)
                session.write_transaction(self._create_is_destination_of, airline, source)
            
    @staticmethod
    def _create_airline(tx, airline):
        
        query = ("MERGE (airline:Airline {name: $airline})")
        
        result = tx.run(query, airline=airline)
    
    @staticmethod
    def _create_city(tx, city):

        coordinates = get_coordinates.get_location(city)
        query = ("MERGE (city:City {name: $city, lat: $lat, lng: $lng})")
        
        result = tx.run(query, city=city, lat=coordinates.latitude, lng=coordinates.longitude)

    @staticmethod
    def _create_has_direct_flight_relationship(tx, source, destination):

        query = (
            "MATCH (a:City {name: $source})"
            "MATCH (b:City {name: $destination})"
            "MERGE (a)-[c:HAS_DIRECT_FLIGHT]->(b)"
            "RETURN a, b, c"
        )
               
        result = tx.run(query, source=source, destination=destination)

        query = (
            "MATCH (a:City {name: $source})"
            "MATCH (b:City {name: $destination})"
            "MERGE (b)-[c:HAS_DIRECT_FLIGHT]->(a)"
            "RETURN a, b, c"
        )
               
        result = tx.run(query, source=source, destination=destination)

    @staticmethod
    def _create_has_operations_in(tx, airline, city):
        
        query = (
            "MATCH (a:City {name: $city})"
            "MATCH (b:Airline {name: $airline})"
            "MERGE (b)-[c:HAS_OPERATIONS_IN]->(a)"
            "RETURN a, b, c"
        )
        
        result = tx.run(query, airline=airline, city=city)
    
    @staticmethod
    def _create_is_destination_of(tx, airline, city):
        
        query = (
            "MATCH (a:City {name: $city})"
            "MATCH (b:Airline {name: $airline})"
            "MERGE (a)-[c:IS_DESTINATION_OF]->(b)"
            "RETURN a, b, c"
        )
        
        result = tx.run(query, airline=airline, city=city)


def insert(source, airlinesWithDestinations):
    
    graphdb = Database(os.environ['NEO4J_URI'], os.environ['NEO4J_USER'], os.environ['NEO4J_PASSWORD'])
    
    graphdb.create_airlines_destinations(source, airlinesWithDestinations)

    graphdb.close()