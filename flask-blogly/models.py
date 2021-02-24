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

    user_posts = db.relationship("Post", backref="User", cascade="all, delete-orphan")

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

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %d %Y, %I:%M %p")


# PostTag Model
class PostTag(db.Model): 
    """ Represents a model between Post and Tag Models. """

    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    tags = db.relationship('Tag', backref='posts_tags')


# Tag Model
class Tag(db.Model):
    """ Represents a tag. """

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    posts = db.relationship(
        'Post',
        secondary='posts_tags',
        backref='tags',
        cascade='all, delete'
    )


def connect_db(app):
    db.app = app
    db.init_app(app)