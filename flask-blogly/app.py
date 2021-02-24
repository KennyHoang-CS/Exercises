"""Blogly application."""

from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag, PostTag


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

    # Add the user and commit the changes. 
    db.session.add(user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """ Delete the user. """

    # Get the user to delete and commit the changes. 
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')


# Handle routes for new user posts. 

@app.route('/users/<int:user_id>/posts/new', methods=["GET"])
def post_form(user_id):
    """ Show form to add a post for that user. """
    
    # Get the current user. 
    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()

    return render_template('post_form.html', user=user, tags=tags)


@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def add_post(user_id):
    """ Handle the form, add post and redirect to user detail page. """

    # Create the new post from form post data. 
    new_post = Post(title=request.form["title"],
                    content=request.form["content"],
                    user_id=user_id)

    # Add the new post and commit the changes. 
    db.session.add(new_post)
    db.session.commit()

    # Get the tag values associated with that new post. 
    tags_values = request.form.getlist('tag')
    tags = [Tag.query.get_or_404(int(tag)) for tag in tags_values]

    # Add the associated tags to that post.
    for tag in tags:
        tag.posts.append(new_post)
        db.session.add(tag)

    # Commit the changes. 
    db.session.commit()
    
    return redirect(f'/users/{user_id}')


# Handle routes to show posts

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """ Show the view of post details. """

    # Get all posts from that user. 
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)

    # Get the list of tags associated with that post_id. 
    tags = list(PostTag.query.filter(PostTag.post_id == post_id))
    
    return render_template('post_details.html', post=post, user=user, tags=tags)

# Handle routes to edit posts. 

@app.route('/posts/<int:post_id>/edit', methods=["GET"])
def show_post_edit_form(post_id):
    """ Show the form to edit post. """

    # Get the user id of that post. 
    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()

    return render_template('post_edit_form.html', post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def update_post(post_id):
    """ Show the form to edit post. """

    # Get the user id of that post. 
    edit_post = Post.query.get_or_404(post_id)

    # Get the form input data. 
    edit_post.title = request.form["title"] or edit_post.title
    edit_post.content = request.form["content"] or edit_post.content

    # Add the edited post and commit the changes. 
    db.session.add(edit_post)
    db.session.commit()

    # Get the tags associated with that edited_post. 
    tags_values = request.form.getlist('tag')
    tags = [Tag.query.get_or_404(int(tag)) for tag in tags_values]

    # Delete the old tag values associated with edit_post. 
    PostTag.query.filter(PostTag.post_id == edit_post.id).delete()

    # Add the fresh new tags to that edited post. 
    for tag in tags:
        tag.posts.append(edit_post)
        db.session.add(tag)

    # Commit the changes. 
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


# Handle routes for tags. 

@app.route('/tags')
def list_tags():
    """ List all tags. """ 

    tags = Tag.query.all()

    return render_template('tags.html', tags=tags)

@app.route('/tags/<int:tag_id>')
def tag_details(tag_id):
    """ Details about a tag. """

    tag = Tag.query.get_or_404(tag_id)
    tags = tag.posts

    return render_template('tag_details.html', tag=tag, tags=tags)

@app.route('/tags/new')
def add_tag():
    """ Show a form to add a new tag. """
    return render_template('new_tag_form.html')

@app.route('/tags/new', methods=["POST"])
def process_tag():
    """ Process the new tag form and add the tag. """

    # Create the new tag.
    new_tag = Tag(name=request.form["name"])
    # Add it to session.
    db.session.add(new_tag)
    # Commit it to database.
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit')
def show_tag_edit_form(tag_id):
    """ Show tag edit form. """

    tag = Tag.query.get_or_404(tag_id)

    return render_template('tag_edit_form.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=["POST"])
def process_tag_edit(tag_id):
    """ Process the tag edit form and edit the tag. """

    # Give the old tag to its new tag name from form input. 
    edit_tag = Tag.query.get(tag_id)
    edit_tag.name = request.form["name"]

    # Add the edited tag and commit the changes. 
    db.session.add(edit_tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def delete_tag(tag_id):
    """ Delete the chosen tag. """
    
    # Delete any references in posts_tags table. 
    PostTag.query.filter(PostTag.tag_id == tag_id).delete()
    # Delete any references in tags table. 
    Tag.query.filter(Tag.id == tag_id).delete()
    # Commit the changes. 
    db.session.commit()
    
    return redirect('/tags')