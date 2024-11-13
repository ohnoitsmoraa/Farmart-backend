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
    f2 = Farmer(name='Jane Smith', email='jane@gmail.com', location='California', farm_name ='Sunshine Farms')
    f3 = Farmer(name='Bob Johnson', email='bon@gmail.com', location='Florida', farm_name ='Golden Fields')
    f4 = Farmer(name='Alice Brown', email='alice@gmail.com', location='New York', farm_name ='Goldy Farms')
    f5 = Farmer(name='Charlie Davis', email='charlie@gmail.com', location='Illinois', farm_name ='Dairy Haven')
    f6 = Farmer(name='Eva Wilson', email='eva@gmail.com', location='Kenti', farm_name ='Evergreen Acres')
    f7 = Farmer(name='Frank Miller', email='frank@gmail.com', location='Oregon', farm_name ='Big Sky Ranch')
    f8 = Farmer(name='Grace Lee', email='grace@gmail.com', location='Washington', farm_name ='Prairie Rose')

    db.session.add_all([f1, f2, f3, f4, f5, f6, f7, f8])
    db.session.commit()

    print ("Seeding farmers data ........")
    