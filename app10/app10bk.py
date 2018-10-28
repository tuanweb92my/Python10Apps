from flask import Flask, render_template, request, send_file
import pandas as pd
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import geocoder
import csv
import pandas as pd
import time

geolocator = Nominatim()

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])

def success():
    global file
    global g
    if request.method == 'POST':
        file = request.files["file"]
        content = request.files['file'].read()
        #content = file.read()
        #print(content)
        #file.save(secure_filename("uploaded"+file.filename))
        print(file)
        print(type(file))

        #df = pd.read_csv(file)
        with open("Supermarket.csv","r") as f, open("Supermarket_result.csv","w",newline='') as g:
        #with open(file,"r") as f, open("Supermarket_result.csv","w",newline='') as g:
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

        #df.to_html("detail_excel.html")
        df = pd.read_csv("Supermarket_result.csv")
        #return render_template("index.html",btn="download.html", text="Please make sure you have an address column in your CSV file.")
        return render_template("index.html",btn="download.html", text="Please make sure you have an address column in your CSV file.",text1=df.to_html())
        #return df.to_html()

@app.route("/download")
def download():
    #return send_file("Updated"+file.filename,attachment_filename="yourfile.csv",as_attachment=True)
    return send_file("Supermarket_result.csv",attachment_filename="theLocationResult.csv",as_attachment=True)

if __name__ == "__main__":
    app.debug=True
    app.run()
