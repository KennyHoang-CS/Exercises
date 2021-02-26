from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """ Form for adding pets. """  

    name = StringField(
        "Pet name", 
        validators=[InputRequired()]
    )
    species = SelectField(
        "Species", 
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)]
    )
    notes = TextAreaField(
        "Notes",
        validators=[Optional()]
    )


class EditPetForm(FlaskForm):
    """ Form to editing pets. """
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )
    notes = TextAreaField(
        "Notes",
        validators=[Optional()]
    )
    available = BooleanField(
        'Available?'
    )
