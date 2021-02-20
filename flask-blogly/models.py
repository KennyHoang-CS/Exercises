"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 
import datetime

db = SQLAlchemy()

# User Model
class User(db.Model):
    """ Represents a user. """
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(100), nullable=False, default="no image")

    posts = db.relationship("Post", backref="User", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """ Return full name of user. """
        return f'{self.first_name} {self.last_name}'


# Post Model
class Post(db.Model):
    """ Represents a post. """

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, 
        nullable=False, 
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

def connect_db(app):
    db.app = app
    db.init_app(app)