from geopy.geocoders import Nominatim

def get_location(city):

    geolocator = Nominatim(user_agent="PlanYourTravel")

    location = geolocator.geocode(city)
    print(city)

    return location