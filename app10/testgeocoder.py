import geocoder
import csv
import pandas as pd
import time

df = pd.read_csv("Supermarket.csv",header=None)
#print(df.head())
for row in df.iterrows():
   g = geocoder.google(row[1])
   #print(g)
   #print(row[1])
   #print(row[1],g.latlng)
   # print(g.latlng)
   # time.sleep(2)

with open("Supermarket.csv","r") as f, open("Supermarket_c.csv","w",newline='') as g:
    rdr = csv.reader(f)
    wtr = csv.writer(g)
    for r in rdr:
        gc = geocoder.google(str(r[1]))
        print(r[1],gc.latlng)
        #print(r + gc.latlng[0]+gc.latlng[1])
        #wtr.writerow(r + gc.latlng[0]+gc.latlng[1])
        time.sleep(2)
