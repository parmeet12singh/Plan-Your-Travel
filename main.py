import requests
from bs4 import BeautifulSoup
import read_wikipedia
import insert_city

import time
start_time = time.time()

# url = 'https://en.wikipedia.org/wiki/Indira_Gandhi_International_Airport'
# url = 'https://en.wikipedia.org/wiki/Kanpur_Airport'
# url = 'https://en.wikipedia.org/wiki/Imphal_Airport'
# url = 'https://en.wikipedia.org/wiki/Ranchi_Airport'
# url = 'https://en.wikipedia.org/wiki/Chhatrapati_Shivaji_Maharaj_International_Airport'
# url = 'https://en.wikipedia.org/wiki/Rajiv_Gandhi_International_Airport'
# url = 'https://en.wikipedia.org/wiki/Veer_Savarkar_International_Airport'
# url = 'https://en.wikipedia.org/wiki/Netaji_Subhas_Chandra_Bose_International_Airport'

city = input('Enter City: ').title()

url = 'https://en.wikipedia.org/wiki/' + city + '_Airport'
response = requests.get(url, verify=False).text

soup = BeautifulSoup(response, 'html.parser')
airport = soup.find("h1",{"class":"firstHeading mw-first-heading"}).text

airlinesWithDestinations = read_wikipedia.read_tables(soup)

print(airport)
print(airlinesWithDestinations)
print(len(airlinesWithDestinations))

insert_city.insert(city, airlinesWithDestinations)


print("--- %s seconds ---" % (time.time() - start_time))