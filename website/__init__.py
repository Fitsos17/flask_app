from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = "PANGER"
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
  db.init_app(app)

  @app.before_first_request
  def create_tables():
    db.create_all()

  from .views import views
  from .auth import auth
  
  app.register_blueprint(views)
  app.register_blueprint(auth)

  return app