from config.database import db
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy


class Token (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(255), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  
    user = db.relationship('User', backref=db.backref('tokens', lazy=True))