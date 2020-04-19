import os
from flask import Flask
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *

# Settings
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://fahyjekubolpsb:084f71e17a72960063160b48657280549094140468ebfe534b9b91b61101a54f@ec2-52-6-143-153.compute-1.amazonaws.com:5432/dacmhgi1g82sc0"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()