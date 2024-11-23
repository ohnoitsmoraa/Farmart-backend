from config.database import db
from sqlalchemy_serializer import SerializerMixin

class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    serialize_rules = ('-user', '-animal',)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="Pending")

    user = db.relationship("User", back_populates="orders")
    animal = db.relationship("Animal", back_populates="order_items")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "animal_id": self.animal_id,
            "total_price": self.total_price,
            "status": self.status,
        }

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, status='{self.status}', total_price={self.total_price})>"
