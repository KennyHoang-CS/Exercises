"""Blogly application."""

from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chicken123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def home():
    """Redirect to list of users."""
    return redirect('/users')

@app.route('/users')
def show_users():
    """ Show all users, view each user details through a link, have link to add user. """
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=["GET"])
def add_user():
    """ Add the user. """
    return render_template('user_form.html')

@app.route('/users/new', methods=["POST"])
def process_user():
    """ Add user to the blogly database. """
    
    # Get the form input data. 
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    # Create the new user with the data.
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    # Add new user to session.
    db.session.add(new_user)

    # Commit the new user to database.
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_details(user_id):
    """ Show details about a single user. """
    user = User.query.get_or_404(user_id)
    return render_template('details.html', user=user)

@app.route('/users/<int:user_id>/edit')
def user_edit(user_id):
    """ Edit the user details. """
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def update_user(user_id):
    """ Update the user with new details. """
    
    user = User.query.get_or_404(user_id)

    # Get the form input data. 
    user.first_name = request.form["first_name"] or user.first_name
    user.last_name = request.form["last_name"] or user.last_name
    user.image_url = request.form["image_url"] or user.image_url

    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """ Delete the user. """

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
