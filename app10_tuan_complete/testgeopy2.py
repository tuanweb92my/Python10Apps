from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder
import csv
import pandas as pd
import time

geolocator = Nominatim()

with open("Supermarket.csv","r") as f, open("Supermarket_result.csv","w",newline='') as g:
    rdr = csv.reader(f)
    headers = next(rdr, None)  # skip the headers
    wtr = csv.writer(g)
    if headers:
        wtr.writerow(headers+['Latitude']+['Longitude'])

    for r in rdr:
        location = geolocator.geocode(str(r[1]), timeout=10)
        print(location.latitude, location.longitude)
        #r = r + [location.latitude] + [location.longitude]
        #print(r)
        wtr.writerow(r + [location.latitude] + [location.longitude])
        #time.sleep(2)
