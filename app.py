from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import *
from config.database import db
from flask_jwt_extended import jwt_required, JWTManager, get_jwt, create_access_token
import os
from dotenv import load_dotenv
from flask_restful import Api, Resource

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
# app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config ['JWT_TOKEN_LOCATION'] = ['headers']

jwt = JWTManager(app)

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)

# Home route
@app.route('/')
def index():
    return '''
        <html>
            <head>
                <style>
                    h1 {
                        font-weight: bold;
                        text-align: center;
                        color: #2c3e50;  /* You can customize the color */
                    }
                </style>
            </head>
            <body>
                <h1>Hello Dearest Farmer</h1>
            </body>
        </html>
    '''


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
    
# Animals route
@app.route('/animals', methods=['GET', 'POST'])
@jwt_required(optional=True)
def animals():
    if request.method == 'GET':
        animals = Animal.query.all()
        response = [animal.to_dict() for animal in animals]
        return make_response(jsonify(response), 200)

    if request.method == 'POST':
        data = request.get_json()

        if not data or not data.get('type') or not data.get('breed') or not data.get('age') or not data.get('price') or not data.get('farmer_id'):
            return make_response(jsonify({'message': 'Missing required fields'}), 404)

        new_animal = Animal(type=data['type'], breed=data['breed'], age=data['age'], price=data['price'], farmer_id=data['farmer_id'])
        db.session.add(new_animal)
        db.session.commit()
        return make_response(jsonify(new_animal.to_dict()), 201)
    
@app.route('/animals/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@jwt_required()
def animal(id):
    if request.method == 'GET':
        animal = Animal.query.get(id)

        if not animal:
            return make_response({"error": "Animal not found"}, 404)

        return make_response(jsonify(animal.to_dict()), 200)

    if request.method == 'DELETE':
        animal = Animal.query.get(id)

        if not animal:
            return make_response({"error": "Animal not found"}, 404)

        db.session.delete(animal)
        db.session.commit()
        return make_response({"message": "Animal deleted successfully"}, 200)

    if request.method == 'PATCH':
        animal = Animal.query.get(id)
        data = request.get_json()

        if not animal:
            return make_response({"error": "Animal not found"}, 404)

        if 'type' in data:
            animal.type = data['type']
        if 'breed' in data:
            animal.breed = data['breed']
        if 'age' in data:
            animal.age = data['age']
        if 'price' in data:
            animal.price = data['price']
        if 'farmer_id' in data:
            animal.farmer_id = data['farmer_id']

        db.session.commit()

        return make_response(jsonify(animal.to_dict()), 200)
    
# Orders route
@app.route('/orders', methods=['GET', 'POST'])
def get_orders():
    orders = Order.query.all()
    response = [order.to_dict() for order in orders]
    return make_response(jsonify(response), 200)

@app.route('/orders/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@jwt_required()
def order(id):
    if request.method == 'GET':
        order = Order.query.get(id)

        if not order:
            return make_response({"error": "Order not found"}, 404)

        return make_response(jsonify(order.to_dict()), 200)

    if request.method == 'DELETE':
        order = Order.query.get(id)

        if not order:
            return make_response({"error": "Order not found"}, 404)

        db.session.delete(order)
        db.session.commit()
        return make_response({"message": "Order deleted successfully"}, 200)

    if request.method == 'PATCH':
        order = Order.query.get(id)
        data = request.get_json()

        if not order:
            return make_response({"error": "Order not found"}, 404)

        if 'user_id' in data:
            order.user_id = data['user_id']
        if 'animal_id' in data:
            order.animal_id = data['animal_id']
        if 'total_price' in data:
            order.total_price = data['total_price']
        if 'status' in data:
            order.status = data['status']

        db.session.commit()

        return make_response(jsonify(order.to_dict()), 200)
    
@app.route('/orders/<int:id>/checkout', methods=['POST'])
@jwt_required()
def checkout(id):
    order = Order.query.get(id)

    if not order:
        return make_response({"error": "Order not found"}, 404)

    order.status = 'Completed'
    db.session.commit()

    return make_response(jsonify(order.to_dict()), 200)


# RESTFUL API
class RegisterUser(Resource):
    def post(self):
        data = request.get_json()
        user = User.get_user_by_username(username=data.get('username'))

        if user is not None:
            return make_response({"error": "Username already exists"}, 400)
        
        new_user = User(username=data.get('username'), email=data.get('email'))
        new_user.set_password(data.get('password'))
        db.session.add(new_user)
        db.session.commit()

        return make_response({"message": "User created successfully"}, 201)

api.add_resource(RegisterUser, '/register')

class LoginUser(Resource):
    def post(self):
        data = request.get_json()
        user = User.get_user_by_username(username=data.get('username'))

        if user is None or not user.check_password(data.get('password')):
            return make_response({"error": "Invalid username or password"}, 401)

        access_token = create_access_token(identity=user.id)
        return make_response({"access_token": access_token}, 200)
    
api.add_resource(LoginUser, '/login')


class LogoutUser(Resource):
    @jwt_required()   # With this you cannot log out without accessing / logging in
    def get(self):
        jwt = get_jwt()
        jti = jwt['jti']

        new_block_list = Token(jti=jti)
        db.session.add(new_block_list)
        db.session.commit()

        return make_response ({"message" : "User logged out successfully"}, 201)


api.add_resource(LogoutUser, '/logout')

class UserResource(Resource):
    # GET method to fetch one or all users
    def get(self, id=None):
        if id:
            user = User.query.get(id)
            if not user:
                return make_response({"error": "User not found"}, 404)
            return make_response(user.to_dict(), 200)
        else:
            users = User.query.all()
            response = [user.to_dict() for user in users]
            return make_response(jsonify(response), 200)
    
    # POST method to create a new user
    def post(self):
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response({"message": "User created successfully"}, 201)
    
    # PATCH method to update a user
    def patch(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)

        data = request.get_json()

        # Update only provided fields
        for attr in data:
            if hasattr(user, attr):
                setattr(user, attr, data[attr])
        
        db.session.commit()
        return make_response(user.to_dict(), 200)

    # DELETE method to delete a user
    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return make_response({"error": "User not found"}, 404)
        
        db.session.delete(user)
        db.session.commit()
        return make_response({"message": "User deleted successfully"}, 200)

api.add_resource(UserResource, '/users', '/users/<int:id>')


if __name__=='__main__':
    app.run(port=5555, debug=True)
