from neo4j import GraphDatabase
import get_coordinates

class Database:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_airlines_destinations(self, source, airlinesWithDestinations):

        with self.driver.session() as session:
            
            # Creating node for source city
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

        print(result)
    
    @staticmethod
    def _create_city(tx, city):

        coordinates = get_coordinates.get_location(city)
        query = ("MERGE (city:City {name: $city, lat: $lat, lng: $lng})")
        
        result = tx.run(query, city=city, lat=coordinates.latitude, lng=coordinates.longitude)

        print(result)

    @staticmethod
    def _create_has_direct_flight_relationship(tx, source, destination):

        query = (
            "MATCH (a:City {name: $source})"
            "MATCH (b:City {name: $destination})"
            "MERGE (a)-[c:HAS_DIRECT_FLIGHT]->(b)"
            "RETURN a, b, c"
        )
               
        result = tx.run(query, source=source, destination=destination)
        
        print(result)        

        query = (
            "MATCH (a:City {name: $source})"
            "MATCH (b:City {name: $destination})"
            "MERGE (b)-[c:HAS_DIRECT_FLIGHT]->(a)"
            "RETURN a, b, c"
        )
               
        result = tx.run(query, source=source, destination=destination)

        print(result)

    @staticmethod
    def _create_has_operations_in(tx, airline, city):
        
        query = (
            "MATCH (a:City {name: $city})"
            "MATCH (b:Airline {name: $airline})"
            "MERGE (b)-[c:HAS_OPERATIONS_IN]->(a)"
            "RETURN a, b, c"
        )
        
        result = tx.run(query, airline=airline, city=city)

        print(result)
    
    @staticmethod
    def _create_is_destination_of(tx, airline, city):
        
        query = (
            "MATCH (a:City {name: $city})"
            "MATCH (b:Airline {name: $airline})"
            "MERGE (a)-[c:IS_DESTINATION_OF]->(b)"
            "RETURN a, b, c"
        )
        
        result = tx.run(query, airline=airline, city=city)

        print(result)


def insert(source, airlinesWithDestinations):
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://cdfb4b46.databases.neo4j.io"
    user = "neo4j"
    password = "mB-WrhgQSZMRqOHQ4p1SoLK2F4Uxpg_AHWwyv9S5274"
    graphdb = Database(uri, user, password)

    # source = 'Jagdalpur'
    # source = 'Ranchi'
    # source = 'Imphal'
    # airlinesWithDestinations = [['Alliance Air', ['Hyderabad', 'Raipur']]]
    # airlinesWithDestinations = [['AirAsia India', ['Bangalore', 'Chennai', 'Delhi', 'Mumbai']], ['Air India', ['Delhi']], ['Alliance Air', ['Bhubaneswar', 'Kolkata']], ['Go First', ['Bangalore', 'Delhi', 'Mumbai']], ['IndiGo', ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Lucknow', 'Mumbai', 'Patna', 'Pune']], ['Vistara', ['Delhi']]]
    # airlinesWithDestinations = [['AirAsia India', ['Delhi', 'Guwahati', 'Kolkata']], ['Air India', ['Aizawl', 'Delhi', 'Dimapur', 'Guwahati', 'Kolkata']], ['Alliance Air', ['Dimapur', 'Guwahati']], ['IndiGo', ['Agartala', 'Ahmedabad', 'Bangalore', 'Delhi', 'Dibrugarh', 'Guwahati', 'Hyderabad', 'Mumbai', 'Kolkata', 'Shillong']]]
    
    graphdb.create_airlines_destinations(source, airlinesWithDestinations)

    graphdb.close()
