from flask_sqlalchemy import SQLAlchemy  
import datetime

db = SQLAlchemy()

# Pet model.  
class Pet(db.Model):
    """ Represents a pet. """
    
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

def connect_db(app):
    db.app = app
    db.init_app(app)


