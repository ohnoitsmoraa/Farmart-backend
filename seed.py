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
# o1 = Order(user_id=1, animal_id=1, quantity=1, total_price=150000)
