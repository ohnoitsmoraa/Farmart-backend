from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import *
from config.database import db
from flask_jwt_extended import jwt_required, JWTManager
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
# app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config ['JWT_TOKEN_LOCATION'] = ['headers']

jwt = JWTManager(app)

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
        response = [farmer.to_dict() for farmer in farmers]
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
    

@app.route('/farmers/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
# @jwt_required()  
def farmer(id):
    # GET method to Retrieve a specific farmer
    if request.method == 'GET':
        farmer = Farmer.query.get(id)

        if not farmer:
            return make_response({"error": "Farmer not found"}, 404)
        
        return make_response(jsonify(farmer.to_dict()), 200)
    
    # DELETE method to Delete a specific farmer
    if request.method == 'DELETE':
        farmer = Farmer.query.get(id)

        if not farmer:
            return make_response({"error": "Farmer not found"}, 404)

        db.session.delete(farmer)
        db.session.commit()
        return make_response({"message": "Farmer deleted successfully"}, 200)
    
    # PATCH method to Update a specific farmer
    if request.method == 'PATCH':
        farmer = Farmer.query.get(id)
        data = request.get_json()

        if not farmer:
            return make_response({"error": "Farmer not found"}, 404)

        # Update only the fields provided in the request
        if 'name' in data:
            farmer.name = data['name']
        if 'email' in data:
            farmer.email = data['email']
        if 'farm_name' in data:
            farmer.farm_name = data['farm_name']
        if 'location' in data:
            farmer.location = data['location']

        db.session.commit()

        return make_response(jsonify(farmer.to_dict()), 200)
    
# User routes
@app.route('/users', methods=['GET', 'POST'])
@jwt_required(optional=True) # Allows access without a token for GET requests
def users():
    if request.method == 'GET':
        users = User.query.all()
        response = [user.to_dict() for user in users] 
        return make_response(jsonify(response), 200)

    if request.method == 'POST':
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response({"message": "Success"}, 201) 

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE']) 
# @jwt_required() 
def get_user(id):
    if request.method == 'GET':
        user = User.query.get(id)

        if not user:
            return make_response({"error": "User not found"}, 404)
        
        return make_response(user.to_dict(), 200)
    
    if request.method == 'DELETE':
        user = User.query.get(id)

        if not user:
            return make_response({"error": "User not found"}, 404)

        db.session.delete(user)
        db.session.commit()
        return make_response({"message": "Success"}, 200)
    
    if request.method == 'PATCH':
        user = User.query.get(id)
        data = request.get_json()

        if not user:
            return make_response({"error": "User not found"}, 404)

        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        
    db.session.commit()
    return make_response(user.to_dict(), 200)
    

if __name__=='__main__':
    app.run(port=5555, debug=True)
