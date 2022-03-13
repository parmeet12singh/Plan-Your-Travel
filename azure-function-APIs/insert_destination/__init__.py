import requests
from bs4 import BeautifulSoup
from . import read_wikipedia
from shared_code import get_coordinates
from . import insert_city

import azure.functions as func

def main(req: func.HttpRequest):

    city = req.params.get('city')
    if not city:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            city = req_body.get('city')

    if city:
        try:
            city = city.title()

            if(get_coordinates.get_location(city) is None):
                return func.HttpResponse("No city with the name "+city+".\nEnter a correct City Name", status_code=404)

            url = 'https://en.wikipedia.org/wiki/' + city + '_Airport'
            response = requests.get(url).text

            soup = BeautifulSoup(response, 'html.parser')
            airport = soup.find("h1",{"class":"firstHeading mw-first-heading"}).text

            airlinesWithDestinations = read_wikipedia.read_tables(soup)

            insert_city.insert(city, airlinesWithDestinations)

            return func.HttpResponse(airport, status_code=200)
        except:
            return func.HttpResponse("Error in Backend - Neo4j\nThe Developer has been notified and is looking into it", status_code=500)
    else:
        return func.HttpResponse("Please pass a City name in the query parameter i.e. city to insert list of direct connectivity flights from the city entered.\ne.g. http://localhost:7071/api/insert_destinations?city=Kanpur",
                status_code=400)