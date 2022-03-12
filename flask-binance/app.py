from flask import Flask,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
import config
from binance.client import Client
from binance.enums import *
#from order import Order
import datetime as dt
from sqlalchemy.orm import Session
app = Flask(__name__)
client=Client(config.API_KEY,config.API_SECRET)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Admin/Desktop/flask-binance/crypto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
@app.route("/")
def index():
    account=client.get_account()
    balances=account['balances']
    return render_template("index.html",my_balances=balances)

class Binance(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    value=db.Column(db.Float())
    if __name__=="__main__":
        app.run(debug=True)