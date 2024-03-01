from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_adoption"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():
    """Show homepage links."""
    pets = Pet.query.all()
    return render_template("index.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add pet form; handle adding new pet to db"""

    form = AddPetForm()

    if form.validate_on_submit():
        pet_name=form.pet_name.data
        species=form.species.data
        url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        pet = Pet(name=pet_name, species=species, photo_url=url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added a {species} named {pet_name}")
        return redirect("/add")
    else:
        return render_template("add-pet.html", form=form)
    
@app.route("/edit/<int:pet_id>", methods=["GET","POST"])
def edit_pet(pet_id):
    """display pet details and allow user to edit them if needed"""
    
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(f"/edit/{pet_id}")
    
    else:
        return render_template("edit-pet.html", form=form, pet=pet)