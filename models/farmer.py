from config.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Farmer(db.Model):
    __tablename__ = "farmers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    farm_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)

    animals = db.relationship("Animal", back_populates="farmer")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'farm_name': self.farm_name,
            'location': self.location
        }

    def __repr__(self):
        return f"<Farmer(id={self.id}, name='{self.name}', farm_name='{self.farm_name}')>"
