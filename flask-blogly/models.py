"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

# User Model
class User(db.Model):
    """ Represents a user. """
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(100), nullable=False, default="no image")

    @property
    def full_name(self):
        """ Return full name of user. """
        return f'{self.first_name} {self.last_name}'


def connect_db(app):
    db.app = app
    db.init_app(app)