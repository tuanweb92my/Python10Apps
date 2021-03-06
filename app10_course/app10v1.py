from flask import Flask, render_template, request, send_file
import pandas as pd
from geopy.geocoders import Nominatim


app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success-table",methods=['POST'])

def success_table():
        return render_template()

@app.route("/download-file/")
def download():
    return send_file()

if __name__ == "__main__":
    app.debug=True
    app.run()
