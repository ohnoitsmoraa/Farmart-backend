from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import *
from config.database import db
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmart.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# Home route
@app.route('/')
def index():
    return 'Hello Dearest Farmer'

# Farmers route
@app.route('/farmers', methods=['GET', 'POST'])
@jwt_required(optional=True)
def get_farmers():
    # GET request to retrieve all farmers
    if request.method == 'GET':
        farmers = Farmer.query.all()
        response = [farmer.dict() for farmer in farmers]
        return make_response(jsonify(response), 200)
    
    # POST request to create a new farmer
    if request.method == 'POST':
        data = request.get_json()

        if not data or not data.get('name') or not data.get('email') or not data.get('farm_name'):
            return make_response(jsonify({'message': 'Missing required fields'}), 404)
        
        new_farmer = Farmer(name=data['name'], email=data['email'], farm_name=data['farm_name'], location=data.get('location'))
        db.session.add(new_farmer)
        db.session.commit()
        return make_response(jsonify(new_farmer.to_dict()), 201)
    

if __name__=='__main__':
    app.run(port=5555, debug=True)
