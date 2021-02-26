from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, Pet, connect_db
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chicken123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def home_page():
    """ List all pets from our pets database. """
    # Get all the pets from pets table database. 
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """ Add a pet to our views and database by using a form. """
    # Get the pet form. 
    form = AddPetForm()
    # If request is a post and form submitted with valid csrf token. 
    if form.validate_on_submit():
        data = {k: v for k,v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else: # Render the form again the form isn't completed. 
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """ Edit a pet and save it to the database by using a form. """
    
    # Get the pet to be edited. 
    pet = Pet.query.get_or_404(pet_id)
    # Set the form object to our pet object in edit pet form. 
    form = EditPetForm(obj=pet)
    # If form is submitted and valid. 
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')
    else: # Render the form again, if form wasn't completed. 
        return render_template('edit_pet_form.html', form=form, pet=pet)
