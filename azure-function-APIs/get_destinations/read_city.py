from neo4j import GraphDatabase

class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def return_source_destinations(self, city):
        with self.driver.session() as session:
            source = session.read_transaction(self._return_source, city)
            destinations = session.read_transaction(self._return_destinations, city)

            return [source, destinations]

    @staticmethod
    def _return_source(tx, city):

        source = []
        
        query = ("MATCH (n:City {name:$city}) RETURN n")
        result = tx.run(query, city=city)
        for i in iter(result):
            for j in iter(i):
                source = source + [j.get('name'), j.get('lat'), j.get('lng')]

        return source

    @staticmethod
    def _return_destinations(tx, city):

        destinations = []

        query = ("MATCH (n:City {name:$city})-[:HAS_DIRECT_FLIGHT]->(m) RETURN m")
        result = tx.run(query, city=city)
        for i in iter(result):
            for j in iter(i):
                destinations.append([j.get('name'), j.get('lat'), j.get('lng')])

        return destinations