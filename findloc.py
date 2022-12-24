import phonenumbers
import opencage
import folium
from location import *
from phonenumbers import geocoder
def fcountry(number):
    pepnumber = phonenumbers.parse(number)
    location = geocoder.description_for_number(pepnumber, "en")
    return(location)

from phonenumbers import carrier
def fserprov(number):
    service_pro= phonenumbers.parse(number)
    return(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
def giveloc(number):
    
    lat=description_for_latitude(number)
    lngpip=description_for_longitude(number)
 
    print(lat,lngpip)

    myMap = folium.Map(location=[lat, lngpip], zoom_start= 9)
    folium.Marker([lat, lngpip], popup=fcountry(number)).add_to(myMap)

    myMap.save("myLocation.html")
    #webbrowser.open('file://' + os.path.realpath("myLocation.html"))
    #time.sleep(20)
    #os.remove("myLocation.html")