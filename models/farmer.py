from config.database import db

class Farmer(db.Model):
    __tablename__ = "farmers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    farm_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=True)

    animals = db.relationship("Animal", back_populates="farmer")

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
