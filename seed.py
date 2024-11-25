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
    f1 = Farmer(name='John Doe', email='john@gmail.com', location='Texas', farm_name ='Green Pastures')
    f1.set_password("jhn233")
    f2 = Farmer(name='Jane Smith', email='jane@gmail.com', location='California', farm_name ='Sunshine Farms')
    f2.set_password("jane@260")
    f3 = Farmer(name='Bob Johnson', email='bon@gmail.com', location='Florida', farm_name ='Golden Fields')
    f3.set_password("bobo_the_GOAT")
    f4 = Farmer(name='Alice Brown', email='alice@gmail.com', location='New York', farm_name ='Goldy Farms')
    f4.set_password("Alicie")
    f5 = Farmer(name='Charlie Davis', email='charlie@gmail.com', location='Illinois', farm_name ='Dairy Haven')
    f5.set_password("charlieCharlz")
    f6 = Farmer(name='Eva Wilson', email='eva@gmail.com', location='Kenti', farm_name ='Evergreen Acres')
    f6.set_password("eve")
    f7 = Farmer(name='Frank Miller', email='frank@gmail.com', location='Oregon', farm_name ='Big Sky Ranch')
    f7.set_password("257006")
    f8 = Farmer(name='Grace Lee', email='grace@gmail.com', location='Washington', farm_name ='Prairie Rose')
    f8.set_password("gracie_acie")

    db.session.add_all([f1, f2, f3, f4, f5, f6, f7, f8])
    db.session.commit()

    print ("Seeding farmers data ........")

    # Create Animals
    a1 = Animal(type='Cow', breed='Jersey', age = 5, price = 20000, farmer_id=1)
    a2 = Animal(type='Goat', breed='Boer', age = 4, price = 8000, farmer_id=2)
    a3 = Animal(type='Sheep', breed='Merino', age = 3, price = 7000, farmer_id=3)
    a4 = Animal(type='Pig', breed='Yorkshire', age = 2, price = 10000, farmer_id=4)
    a5 = Animal(type='Chicken', breed='Leghorn', age = 1, price = 300, farmer_id=5)
    a6 = Animal(type='Duck', breed='Pekin', age = 1, price = 500, farmer_id=6)
    a7 = Animal(type='Alpaca', breed='Huacaya', age = 4, price = 17000, farmer_id=7)
    a8 = Animal(type='Horse', breed='Arabian', age = 6, price = 25000, farmer_id=8)
    a9 = Animal(type='Donkey', breed='Miniature', age = 7, price = 12000, farmer_id=1)
    a10 = Animal(type='Rabbit', breed='Angora', age = 1, price = 1500, farmer_id=2)
    a11 = Animal(type='Cat', breed='Siamese', age =1, price = 1500, farmer_id=3)

    db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11])
    db.session.commit()

    print ("Seeding animals data..........")

    # Create User
    u1 = User(name='Maureen Nyamamba', email='maureen@gmail.com')
    u1.set_password("momo006")
    u2 = User(name='Abiud Kiprotich', email='abiud@gmail.com' )
    u2.set_password("abiu")
    u3 = User(name='Kevin Kamundi', email='kevin@gmail.com' )
    u3.set_password("kevo")
    u4 = User(name='Nellie Matu', email='nellie@gmail.com')
    u4.set_password("Nels")
    u5 = User(name='Mitchelle Tamnai', email='mitchelle@gmail.com')
    u5.set_password("Mitch")
    u6 = User(name='Tony Audii', email='tony@gmail.com' )
    u6.set_password("Tosh")
    u7 = User(name='Kipkorir Kyll ', email='kipkorir@gmail.com' )
    u7.set_password("Kyl")
    u8 = User(name='Augo Martin', email='augo@gmail.com' )
    u8.set_password("Augs")
    u9 = User(name='Kimberly Achieng', email='kimberly@gmail.com')
    u9.set_password("Kim")

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




