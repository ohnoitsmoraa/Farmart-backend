from app import app
from models import *
from config.database import db

with app.app_context():

    # clear existing data to prevent duplication
    db.session.query(Farmer).delete()
    db.session.query(Animal).delete()
    db.session.query(User).delete()
    db.session.query(Order).delete()
    db.session.query(Cart).delete()

    db.session.commit()

    print ("Seeding data ..............")

    # Create Farmers
    f1 = Farmer(name='John Doe', email='john@gmail.com', location='Texas', farm_name ='Green Pastures', password="jhn233")
    f2 = Farmer(name='Jane Smith', email='jane@gmail.com', location='California', farm_name ='Sunshine Farms', password="jane@260")
    f3 = Farmer(name='Bob Johnson', email='bon@gmail.com', location='Florida', farm_name ='Golden Fields', password="bobo_the_GOAT")
    f4 = Farmer(name='Alice Brown', email='alice@gmail.com', location='New York', farm_name ='Goldy Farms', password="alice_got_nyash")
    f5 = Farmer(name='Charlie Davis', email='charlie@gmail.com', location='Illinois', farm_name ='Dairy Haven', password="charliecharlz")
    f6 = Farmer(name='Eva Wilson', email='eva@gmail.com', location='Kenti', farm_name ='Evergreen Acres', password="eve")
    f7 = Farmer(name='Frank Miller', email='frank@gmail.com', location='Oregon', farm_name ='Big Sky Ranch', password="257006")
    f8 = Farmer(name='Grace Lee', email='grace@gmail.com', location='Washington', farm_name ='Prairie Rose', password="gracie_acie")

    db.session.add_all([f1, f2, f3, f4, f5, f6, f7, f8])
    db.session.commit()

    print ("Seeding farmers data ........")

    # Create Animals
    a1 = Animal(type='Cow', breed='Jersey', age = 2, price = 150000, farmer_id=1)
    a2 = Animal(type='Goat', breed='Angus', age = 3, price = 16000, farmer_id=2)
    a3 = Animal(type='Sheep', breed='Hereford', age = 5, price = 13000, farmer_id=3)
    a4 = Animal(type='Pig', breed='Landrace', age = 7, price = 14000, farmer_id=4)
    a5 = Animal(type='Chicken', breed='Leghorn', age = 4, price = 1800, farmer_id=5)
    a6 = Animal(type='Duck', breed='Pekin', age = 9, price = 17000, farmer_id=6)
    a7 = Animal(type='Donkey', breed='Mule', age = 4, price = 19000, farmer_id=7)
    a8 = Animal(type='Horse', breed='Shetland', age = 3, price = 200000, farmer_id=8)
    a9 = Animal(type='Cow', breed='Freshian', age = 3, price = 170000, farmer_id=1)
    a10 = Animal(type='Goat', breed='Angora', age = 3, price = 18000, farmer_id=2)
    a11 = Animal(type='Sheep', breed='Dorper', age =6, price = 15000, farmer_id=3)

    db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11])
    db.session.commit()

    print ("Seeding animals data..........")

    # Create User
    u1 = User(name='Maureen', email='maureen@gmail.com', password="momo006")
    u2 = User(name='Abiud', email='abiud@gmail.com', password="abiud254")
    u3 = User(name='Kevin', email='kevin@gmail.com', password="kevo_dealer")
    u4 = User(name='Nellie', email='nellie@gmail.com', password="NelzMtz")
    u5 = User(name='Mitchelle', email='mitchelle@gmail.com', password="Mitch")
    u6 = User(name='Tony', email='tony@gmail.com', password="tony_bliss")
    u7 = User(name='Kipkorir', email='kipkorir@gmail.com', password="KipKip")
    u8 = User(name='Augo', email='augo@gmail.com', password="Aug2")
    u9 = User(name='Kimberly', email='kimberly@gmail.com', password="Kim_got_berly")

    db.session.add_all([u1, u2, u3, u4, u5, u6, u7, u8, u9])
    db.session.commit()

    print ("Seeding users data..........")

    # Create Orders
    o1 = Order(user_id=8, animal_id=1,  total_price=300000, status='available')
    o2 = Order(user_id=7, animal_id=2,  total_price=64000, status='pending')
    o3 = Order(user_id=6, animal_id=3,  total_price=65000, status='sold')
    o4 = Order(user_id=5, animal_id=4,  total_price=42000, status='available')
    o5 = Order(user_id=4, animal_id=5,  total_price=9000, status='pending')
    o6 = Order(user_id=3, animal_id=6,  total_price=68000, status='sold')
    o7 = Order(user_id=2, animal_id=7,  total_price=38000, status='available')
    o8 = Order(user_id=1, animal_id=8,  total_price=200000, status='pending')

    db.session.add_all([o1, o2, o3, o4, o5, o6, o7, o8])
    db.session.commit()

    print ("Seeding orders data..........")

    # Create Cart
    c1 = Cart(user_id=1, animal_id=1)
    c2 = Cart(user_id=2, animal_id=2)
    c3 = Cart(user_id=3, animal_id=3)
    c4 = Cart(user_id=4, animal_id=4) 
    c5 = Cart(user_id=5, animal_id=5) 
    c6 = Cart(user_id=6, animal_id=6) 
    c7 = Cart(user_id=7, animal_id=7) 
    c8 = Cart(user_id=8, animal_id=8)

    db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8])
    db.session.commit()

    print("Seeding completed ❤️")




