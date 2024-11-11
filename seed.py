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

    