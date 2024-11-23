from config.database import db
from sqlalchemy_serializer import SerializerMixin

class Cart(db.Model, SerializerMixin):
    __tablename__ = "cart"

    serialize_rules = ('-user', '-animal',)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"), nullable=False)

    user = db.relationship("User", back_populates="cart_items")
    animal = db.relationship("Animal", back_populates="cart_items")

    def __repr__(self):
        return f"<Cart(id={self.id}, user_id={self.user_id}, animal_id={self.animal_id})>"
