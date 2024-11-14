from config.database import db

class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    breed = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmers.id"), nullable=False)

    farmer = db.relationship("Farmer", back_populates="animals")
    cart_items = db.relationship("Cart", back_populates="animal")
    order_items = db.relationship("Order", back_populates="animal")

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "breed": self.breed,
            "age": self.age,
            "price": self.price,
            "farmer_id": self.farmer_id,
        }

    def __repr__(self):
        return f"<Animal(id={self.id}, type='{self.type}', breed='{self.breed}', price={self.price})>"
