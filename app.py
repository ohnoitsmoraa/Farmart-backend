from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import *
from config.database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmart.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Hello Dearest Farmer'

# @app.route('/farmers')
