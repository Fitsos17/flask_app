from sqlalchemy.sql import func
from . import db

class User(db.Model):
  user_id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(60))
  email = db.Column(db.String(60), unique=True)
  password = db.Column(db.String(30))
  note_id = db.relationship("Note")

class Note(db.Model):
  note_id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(10000))
  date = db.Column(db.DateTime, default=func.now)
  user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))