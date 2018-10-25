from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)

#local database on 127.0.0.1
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'

#database on heroku :
app.config['SQLALCHEMY_DATABASE_URI']='postgres://rkrdpytcoxivht:32183447cf82c434e8c6c69583c235f30fcfdc66724788e13d5f8ac45a7d46af@ec2-184-73-222-192.compute-1.amazonaws.com:5432/dcvrq4ouh7j9f9?sslmode=require'

db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_


@app.route("/")

def index():
    return render_template("index.html")

@app.route("/success",methods=['POST'])

def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        print(email,height)
        #send_email(email,height)
        #print(height)
        #print(request.form)
        #print(db.session.query(Data).filter(Data.email_==email))
        #print(db.session.query(Data).filter(Data.email_==email).count())
        #print(type(db.session.query(Data).filter(Data.email_==email).count()))
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count = db.session.query(Data.height_).count()
            send_email(email,height,average_height,count)
            print(average_height)
            return render_template("success.html")
    return render_template("index.html",
     text="Seems like we've got something from that email address already ")

if __name__ == "__main__":
    app.debug=True
    app.run()
