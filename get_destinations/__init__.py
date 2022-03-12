import azure.functions as func
import json
from . import read_city
import os

def main(req: func.HttpRequest):

    source = req.params.get('city')
    if not source:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            source = req_body.get('city')

    if source:
        try:
            source = source.title()
            
            app = read_city.App(os.environ['NEO4J_URI'], os.environ['NEO4J_USER'], os.environ['NEO4J_PASSWORD'])

            source_destinations = app.return_source_destinations(source)
            
            destinations = {}
            for i in source_destinations[1]:
                destinations[i[0]] = {
                    "lat": i[1],
                    "lng": i[2]
                }

            source_destinations = json.dumps({
                "source": {
                    "name": source_destinations[0][0],
                    "lat": source_destinations[0][1],
                    "lng": source_destinations[0][2]
                },
                "destinations": destinations
            })

            app.close()

            return func.HttpResponse(source_destinations, mimetype='application/json', status_code=200)
        except:
            return func.HttpResponse("Error in Backend - Neo4j\nThe Developer has been notified and is looking into it", status_code=500)
    else:
        return func.HttpResponse("Please pass a City name in the query parameter i.e. city for a JSON list of direct connectivity flights from the city entered.\ne.g. http://localhost:7071/api/get_destinations?city=Kanpur",
             status_code=400)