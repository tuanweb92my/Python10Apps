from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder
import csv
import pandas as pd
import time

#my_address = '212 nguyen van nguyen st, district 1,  ho chi minh, vietnam'

geolocator = Nominatim()
#location = geolocator.geocode(my_address, timeout=10)
#print(location.latitude, location.longitude)

#df = pd.read_csv("Supermarket.csv",header=None)
#df = pd.read_csv("Supermarket.csv",header=1)

headers = read.csv(file, skip = 1, header = F, nrows = 1, as.is = T)
df = read.csv(file, skip = 3, header = F)
colnames(df)= headers

with open("Supermarket.csv","r") as f, open("Supermarket_result.csv","w",newline='') as g:
    rdr = csv.reader(f,skip=2)
    wtr = csv.writer(g)
    for r in rdr[1:]:
        #gc = geocoder.google(str(r[1]))
        location = geolocator.geocode(str(r[1]), timeout=10)
        #print(r[1],gc.latlng)
        print(location.latitude, location.longitude)
        #print(r + gc.latlng[0]+gc.latlng[1])
        #wtr.writerow(r + gc.latlng[0]+gc.latlng[1])
        r = r + [location.latitude] + [location.longitude]
        print(r)
        wtr.writerow(r + [location.latitude] + [location.longitude])
        #time.sleep(2)
