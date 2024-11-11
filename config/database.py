from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance (this will be tied to the Flask app in app.py)
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
