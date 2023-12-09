from flask import Blueprint, render_template, request, redirect, url_for, flash
import flask_login
from . import db
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
import pathlib
from flask import current_app

from . import model

MAIN_PHOTOS_FOLDER = "/static/main_photos"

bp = Blueprint("recipe", __name__)

@bp.route("/create_recipe")
@flask_login.login_required
def create_recipe():
    return render_template("recipe/create_recipe.html")

@bp.route("/create_recipe", methods=["POST"])
def create_recipe_post():
    title = request.form.get("title")
    description = request.form.get("description")
    n_person = request.form.get("n_person")
    cooking_time = request.form.get("cooking_time")
    dificulty = request.form.get("dificulty")
    user = flask_login.current_user
    new_recipe = model.Recipes(user_id = user.id, title = title, description = description,
    n_person = n_person, cooking_time=cooking_time, dificulty=dificulty, user = user)
    db.session.add(new_recipe)
    db.session.commit()

   #main photo: 
    uploaded_file = request.files['main_photo']
  #check that the photo has been correctly updated:  
    if uploaded_file.filename == '':
        flash("No file selected")
        return redirect(url_for("recipe.create_recipe"))

    content_type = uploaded_file.content_type
    if content_type == "image/png":
        file_extension = "png"
    elif content_type == "image/jpeg":
        file_extension = "jpg"
    else:
        flash("The Content-Time of the image is not supported")
        return redirect(url_for("recipe.create_recipe"))

    filename = str(new_recipe.id)+ "."+ file_extension

    path = (pathlib.Path(current_app.root_path)/"static"/ "main_photos"/filename)
    uploaded_file.save(path)

    new_recipe.main_photo = filename
    db.session.commit()

   # we need to get all the ingredients from Ingredients:
    existing_ingredients = Ingredients.query.all()
    return render_template("recipe/recipe_interm.html", recipe_id=new_recipe.id, existing_ingredients=existing_ingredients)


@bp.route("/recipe_interm/<int:recipe_id>")
@flask_login.login_required
def recipe_interm(recipe_id):
    recipe = db.get_or_404(model.Recipes, recipe_id)
    return render_template("recipe/create_recipe.html")

@bp.route("/recipe_interm/<int:recipe_id>", methods=["POST"])
@flask_login.login_required
def recipe_interm_post(recipe_id):
    if request.form.get("add_ingredient"):
        ingredient_name = request.form.get("ingredient")
        quantity = request.form.get("quantity")
        units = request.form.get("units")
       #check if exits:
       ingredient = Ingredients.query.filter_by(name = ingredient_name).first()
       if not ingredient:
            ingredient = model.Ingredients(name = ingredient_name)
            db.session.add(ingredient)
            db.session.commit()
        
        existing_ingredients = Ingredients.query.all()
        quantified_ingredient = model.QuantifiedIngredients(number = quantity, unit_measurement = units,
        ingredients_id = ingredient.id, recipes_id = recipe_id)

        db.session.add(quantified_ingredient)
        db.session.commit()
        return redirect(url_for("recipe.recipe_interm", recipe_id=recipe_id, existing_ingredients = existing_ingredients))
    
    else if request.form.get("steps"):
      #check how many steps are already
        existing_steps = Steps.query.filter_by(recipe_id=recipe_id).count()
        seq_n = existing_steps + 1

        step = request.form.get("step_description")
        new_step = model.Steps(description = step, sequence_number = seq_n, recipe_id = recipe_id)

        db.session.add(new_step)
        db.session.commit()
        return redirect(url_for("recipe.recipe_interm", recipe_id=recipe_id))

    else if "mark_complete" in request.form:
        return render_template("recipe/recipe.html", recipe_id = recipe_id)

@bp.route("/recipe/<int:recipe_id>")
@flask_login.login_required
def recipe(recipe_id):
    recipe = db.get_or_404(model.Recipes, recipe_id)
    return render_template("recipe/recipe.html", recipe = recipe)

"""@bp.route("/recipe1")
def recipe1():
    Esto es solo un ejemplo de como se vería una receta, pero hay que ver como hacer para que cuando se de click a una, se 
    forme la vista
    r = model.RecipePreuba(recipe_id = 1, user = "Mary", title = "Gingerbread Cookies", photo = "static/recipe1.jpg", 
    description = "Delicius cookies for doing on christmas", cooking_time = 40, n_persons = 4, dificulty = "Easy", 
    ingredients = ["5 Eggs", "500 gr Flour", "Ginger", "50 gr Sugar"], steps = ["Beat the eggs", "Take a spoon", "Turn on the oven", "Decorate"],
    other_photos =["static/ou1.jpg", "static/ou2.jpeg"] )
    return render_template("recipe/recipe.html", recipe = r)

@bp.route("/recipe1", methods=["POST"])
def recipe1_post():
    r = request.form.get("rating")"""

