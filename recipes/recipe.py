from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login
from flask_login import current_user

from . import model

MAIN_PHOTOS_FOLDER = "/static/main_photos"

bp = Blueprint("recipe", __name__)

@bp.route("/create_recipe")
@flask_login.login_required
def create_recipe():
    return render_template("main/create_recipe.html")

@bp.route("/create_recipe", methods=["POST"])
def create_recipe_post():
    title = request.form.get("title")
    description = request.form.get("description")
    n_person = request.form.get("n_person")
    cooking_time = request.form.get("cooking_time")
    dificulty = request.form.get("dificulty")
    user = current_user
    new_recipe = model.Recipe(user = user, user_id = user.id, title = title, description = description,
    n_person = n_person, cooking_time=cooking_time, dificulty=dificulty)
    db.session.add(new_recipe)
    db.session.commit()

    main_photo = request.files['main_photo']
    recipe_id = recipe.id
    filename = secure_filename(str(recipe_id))
    main_photo.save(os.path.join(MAIN_PHOTOS_FOLDER, filename))

    # Actualizar la receta en la base de datos con la ruta de la imagen
    new_recipe.main_photo = filename
    db.session.commit()

    
   #render template -> segunda parte del form donde se añaden los ingredientes 
    return render_template("main/create_recipe.html")

@bp.route("/recipe1")
def recipe1():
    """Esto es solo un ejemplo de como se vería una receta, pero hay que ver como hacer para que cuando se de click a una, se 
    forme la vista"""
    r = model.RecipePreuba(recipe_id = 1, user = "Mary", title = "Gingerbread Cookies", photo = "static/recipe1.jpg", 
    description = "Delicius cookies for doing on christmas", cooking_time = 40, n_persons = 4, dificulty = "Easy", 
    ingredients = ["5 Eggs", "500 gr Flour", "Ginger", "50 gr Sugar"], steps = ["Beat the eggs", "Take a spoon", "Turn on the oven", "Decorate"],
    other_photos =["static/ou1.jpg", "static/ou2.jpeg"] )
    return render_template("main/recipe.html", recipe = r)

@bp.route("/recipe1", methods=["POST"])
def recipe1_post():
    r = request.form.get("rating")

