from flask import Flask, render_template, request, send_file
import pandas as pd
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# from send_email import send_email
from sqlalchemy.sql import func
from werkzeug import secure_filename

app = Flask(__name__)

#local database on 127.0.0.1
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'

#database on heroku :
#app.config['SQLALCHEMY_DATABASE_URI']='postgres://rkrdpytcoxivht:32183447cf82c434e8c6c69583c235f30fcfdc66724788e13d5f8ac45a7d46af@ec2-184-73-222-192.compute-1.amazonaws.com:5432/dcvrq4ouh7j9f9?sslmode=require'

#db = SQLAlchemy(app)

# #class Data(db.Model):
#     __tablename__="data"
#     id=db.Column(db.Integer,primary_key=True)
#     email_=db.Column(db.String(120),unique=True)
#     height_=db.Column(db.Integer)
#
#     def __init__(self,email_,height_):
#         self.email_=email_
#         self.height_=height_


@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])

def success():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        #content = file.read()
        #print(content)
        file.save(secure_filename("uploaded"+file.filename))
        print(file)
        print(type(file))
        #file.save("uploaded"+file.filename)
        # with open("uploaded"+file.filename,"a") as f:
        #     f.write("This was added later!")
        #return render_template("success.html")
        df = pd.read_excel(file)

        df.to_html("detail_excel.html")

        #df = pd.read_excel(file)
        #return render_template("index.html",btn="download.html", text="Please make sure you have an address column in your CSV file.")
        return render_template("index.html",btn="download.html", text="Please make sure you have an address column in your CSV file.",text1=df.to_html())
        #return df.to_html()

@app.route("/download")
def download():
    return send_file("uploaded"+file.filename,attachment_filename="yourfile.csv",as_attachment=True)

if __name__ == "__main__":
    app.debug=True
    app.run()
