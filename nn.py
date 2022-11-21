from numpy import number
import phonenumbers
import folium
from phonenumbers import geocoder
key = '8d1df9276d2445c5a93c8b12ce962b1e'


number = "+919813729567"

theNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(theNumber, "en")

print(yourLocation)


#Other details

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query =str(yourLocation)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']

long = results[0]['geometry']['lat']

print(lat, long)


myMap = folium.Map(location =[lat, long], zoom_start_= 9)

folium.Marker([lat , long], popup=  yourLocation).add_to(myMap)


#html save
myMap.save("myLoc.html")
