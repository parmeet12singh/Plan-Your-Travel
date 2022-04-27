from neo4j import GraphDatabase
import json

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

    def get_properties(self):
        return self._properties

if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://cdfb4b46.databases.neo4j.io"
    user = "neo4j"
    password = "mB-WrhgQSZMRqOHQ4p1SoLK2F4Uxpg_AHWwyv9S5274"
    app = App(uri, user, password)

    source = input('Enter city: ').title()
    source_destinations = app.return_source_destinations(source)
    
    destinations = {}
    for i in source_destinations[1]:
        destinations[i[0]] = {
            "lat": i[1],
            "lng": i[2]
        }

    ans = json.dumps({
        "source": {
            "name": source_destinations[0][0],
            "lat": source_destinations[0][1],
            "lng": source_destinations[0][2]
        },
        "destinations": destinations
    })

    print(ans)

    app.close()