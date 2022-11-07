from sqlalchemy.sql import func
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(60))
  email = db.Column(db.String(60), unique=True)
  password = db.Column(db.String(30))
  notes = db.relationship("Note")

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default=func.now())
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))