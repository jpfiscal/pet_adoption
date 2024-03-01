from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf, URL

class AddPetForm(FlaskForm):
    """Form for adding new pets to the adoption system"""
    
    pet_name = StringField("Pet Name",
                           validators=[InputRequired()])
    species = StringField("Species",
                           validators=[InputRequired(),
                                       AnyOf(values=["cat","dog","porcupine","swan"], message="We only accept dogs, cats, swans and porcupines.")])
    photo_url = StringField("Photo URL",
                            validators=[Optional(),
                            URL(message="Invalid URL format.")])
    age = IntegerField("Age",
                           validators=[Optional(), 
                                       NumberRange(min=0, max=30, message="Age must be between 0 and 30 years old.")])
    notes = TextAreaField("Notes",
                           validators=[Optional()])
    
class EditPetForm(FlaskForm):
    """Form for adding new pets to the adoption system"""
    
    photo_url = StringField("Photo URL",
                            validators=[Optional(),
                            URL(message="Invalid URL format.")])
    notes = TextAreaField("Notes",
                           validators=[Optional()])
    available = BooleanField("Available")