from app import app
from models import *

with app.app_context():

# clear existing data to prevent duplication
db_session.query(Farmer).delete()
db_session.query(Animal).delete()
db_session.query(User).delete()
db_session.query(Order).delete()
db_session.query(Cart).delete()

db_session.commit()

# Create Farmers
f1 = Farmer(name='John Doe', email='john@gmail.com', location='Texas', farm_name ='Green Pastures' , password= 'Johdoe987')
f2 = Farmer(name='Jane Smith', email='jane@gmail.com', location='California', farm_name ='Sunshine Farms',  password= 'janesmith35')
f3 = Farmer(name='Bob Johnson', email='bon@gmail.com', location='Florida', farm_name ='Golden Fields' , password='bobson987')
f4 = Farmer(name='Alice Brown', email='alice@gmail.com', location='New York', farm_name ='Goldy Farms', password='aliceb467')
f5 = Farmer(name='Charlie Davis', email='charlie@gmail.com', location='Illinois', farm_name ='Dairy Haven', password='chaldav987')
f6 = Farmer(name='Eva Wilson', email='eva@gmail.com', location='Kenti', farm_name ='Evergreen Acres', password='evawil879')
f7 = Farmer(name='Frank Miller', email='frank@gmail.com', location='Oregon', farm_name ='Big Sky Ranch', password='frankmil7656')
f8 = Farmer(name='Grace Lee', email='grace@gmail.com', location='Washington', farm_name ='Prairie Rose', password='gracelee356')

db_session.add_all([f1, f2, f3, f4, f5, f6, f7, f8])
db_session.commit()

 # Create Animals
a1 = Animal(name='Cow', breed='Jersey', price = 150000, status ='available' , farmer_id=1)
a2 = Animal(name='Goat', breed='Angus', price = 16000, status ='available', farmer_id=2)
a3 = Animal(name='Sheep', breed='Hereford', price = 13000, status ='available', farmer_id=3)
a4 = Animal(name='Pig', breed='Landrace', price = 14000, status ='available', farmer_id=4)
a5 = Animal(name='Chicken', breed='Leghorn', price = 1800, status ='available', farmer_id=5)
a6 = Animal(name='Duck', breed='Pekin', price = 17000, status ='available', farmer_id=6)
a7 = Animal(name='Donkey', breed='Mule', price = 19000, status ='available', farmer_id=7)
a8 = Animal(name='Horse', breed='Shetland', price = 200000, status ='available', farmer_id=8)
a9 = Animal(name='Cow', breed='Freshian', price = 170000, status ='available', farmer_id=1)
a10 = Animal(name='Goat', breed='Angora', price = 18000, status ='available', farmer_id=2)
a11 = Animal(name='Sheep', breed='Dorper', price = 15000, status ='available', farmer_id=3)

db_session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11])
db_session.commit()

# Create User
u1 = User(name='Maureen', email='maureen@gmail.com', location='Texas', password ='Mr1234')
u2 = User(name='Abiud', email='abiud@gmail.com', location='California', password ='John15934')
u3 = User(name='Kevin', email='kevin@gmail.com', location='Florida', password ='Abiud1234')
u4 = User(name='Nellie', email='nellie@gmail.com', location='New York', password ='Abiud1234')
u5 = User(name='Mitchelle', email='mitchelle@gmail.com', location='Illinois', password ='Abiud1234')
u6 = User(name='Tony', email='tony@gmail.com', location='Kenti', password ='Kent578')
u7 = User(name='Kipkorir', email='kipkorir@gmail.com', location='Oregon', password ='Kipr986')
u8 = User(name='Augo', email='augo@gmail.com', location='Washington', password ='Aug8234')
u9 = User(name='Kimberly', email='kimberly@gmail.com', location='Texas', password ='Kim34')

db_session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9])
db_session.commit()

# Create Orders
o1 = Order(user_id=8, animal_id=1, quantity=2, total_price=300000)
o2 = Order(user_id=7, animal_id=2, quantity=4, total_price=64000)
o3 = Order(user_id=6, animal_id=3, quantity=5, total_price=65000)
o4 = Order(user_id=5, animal_id=4, quantity=3, total_price=42000)
o5 = Order(user_id=4, animal_id=5, quantity=5, total_price=9000)
o6 = Order(user_id=3, animal_id=6, quantity=4, total_price=68000)
o7 = Order(user_id=2, animal_id=7, quantity=2, total_price=38000)
o8 = Order(user_id=1, animal_id=8, quantity=1, total_price=200000)

db_session.add_all([o1, o2, o3, o4, o5, o6, o7, o8])
db_session.commit()

# Create Cart
c1 = Cart(user_id=1, animal_id=1, quantity=2, total_price=300000)
c2 = Cart(user_id=2, animal_id=2, quantity=4, total_price=64000)
c3 = Cart(user_id=3, animal_id=3, quantity=5, total_price=65000)
c4 = Cart(user_id=4, animal_id=4, quantity=3, total_price=42000)
c5 = Cart(user_id=5, animal_id=5, quantity=5, total_price=9000)
c6 = Cart(user_id=6, animal_id=6, quantity=4, total_price=68000)
c7 = Cart(user_id=7, animal_id=7, quantity=2, total_price=38000)
c8 = Cart(user_id=8, animal_id=8, quantity=1, total_price=200000)

db_session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])
db_session.commit()

# Create farmers
f1 = Farmer(name="John Doe")
f2 = Farmer(name="Jane Smith")

db_session.add_all([f1, f2])
db_session.commit()

# Add Farmers to Animals
a1.farmer.append(f1)
a2.farmer.append(f2)
a3.farmer.append(f1)

# Add Animals to Farmers
f1.animals.append(a1)
f1.animals.append(a3)
f2.animals.append(a2)

db_session.commit()


