from geopy.geocoders import Nominatim

def get_location(city):

    geolocator = Nominatim(user_agent="PlanYourTravel")

    location = geolocator.geocode(city)

    if(location is not None):
        print('not empty')
    else:
        print('empty')

    print(city)
    print(location)
    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)

    return location

get_location('le')