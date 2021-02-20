"""Blogly application."""

from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post


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

# Handle routes for users: to list, to add, to delete.  

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
    posts = Post.query.filter_by(user_id=user_id).all()
    return render_template('details.html', user=user, posts=posts)

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


# Handle routes for new user posts. 

@app.route('/users/<int:user_id>/posts/new', methods=["GET"])
def post_form(user_id):
    """ Show form to add a psot for that user. """
    
    # Get the current user. 
    user = User.query.get_or_404(user_id)

    return render_template('post_form.html', user=user)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """ Handle the form, add post and redirect to user detail page. """

    # Get the current user. 
    #user = User.query.get_or_404(user_id)

    new_post = Post(title=request.form["title"],
                    content=request.form["content"],
                    user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')


# Handle routes to show posts

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """ Show the view of post details. """

    # Get all posts from that user. 
    #posts = Post.query.filter_by(user_id=user_id).all()
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)

    return render_template('post_details.html', post=post, user=user)

# Handle routes to edit posts. 

@app.route('/posts/<int:post_id>/edit', methods=["GET"])
def show_post_edit_form(post_id):
    """ Show the form to edit post. """

    # Get the user id of that post. 
    post = Post.query.get_or_404(post_id)

    return render_template('post_edit_form.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def update_post(post_id):
    """ Show the form to edit post. """

    # Get the user id of that post. 
    post = Post.query.get_or_404(post_id)

    # Get the form input data. 
    post.title = request.form["title"] or post.title
    post.content = request.form["content"] or post.content

    db.session.add(post)
    db.session.commit()

    return redirect(f'/posts/{post_id}')

# Handle routes to delete posts. 
@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    """ Delete a post. """

    # Get the user id of that post. 
    post = Post.query.get_or_404(post_id)
    
    # Delete the post from database. 
    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')