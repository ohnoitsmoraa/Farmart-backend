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
f1 = Farmer(name='John Doe', email='john@gmail.com', location='Texas', farm_name ='Green Pastures')
f2 = Farmer(name='Jane Smith', email='jane@gmail.com', location='California', farm_name ='Sunshine Farms')
f3 = Farmer(name='Bob Johnson', email='bon@gmail.com', location='Florida', farm_name ='Golden Fields')
f4 = Farmer(name='Alice Brown', email='alice@gmail.com', location='New York', farm_name ='Goldy Farms')
f5 = Farmer(name='Charlie Davis', email='charlie@gmail.com', location='Illinois', farm_name ='Dairy Haven')
f6 = Farmer(name='Eva Wilson', email='eva@gmail.com', location='Kenti', farm_name ='Evergreen Acres')
f7 = Farmer(name='Frank Miller', email='frank@gmail.com', location='Oregon', farm_name ='Big Sky Ranch')
f8 = Farmer(name='Grace Lee', email='grace@gmail.com', location='Washington', farm_name ='Prairie Rose')

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
