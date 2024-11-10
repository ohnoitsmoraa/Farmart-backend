from config.database import db

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default="Pending")

    user = db.relationship("User", back_populates="orders")
    animal = db.relationship("Animal", back_populates="order_items")

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, status='{self.status}', total_price={self.total_price})>"
