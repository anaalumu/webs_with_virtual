import datetime
import dateutil.tz

from flask import Blueprint, render_template
from flask_login import current_user

from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """user = model.User(name = "Mary", password = "1234", email = "mary@example.com")
    r = model.Recipe(user_id = 1, title = "Gingerbread Cookies", main_photo = "static/recipe1.jpg", 
    description = "Delicius cookies for doing on christmas", cooking_time = 40, n_person = 4, dificulty = "Easy", 
                     quantified_ingredients = ["5 Eggs", "500 gr Flour", "Ginger", "50 gr Sugar"], steps = ["Beat the eggs", "Take a spoon", "Turn on the oven", "Decorate"]) 
       # model.Recipe(2, user, "Stuffed Chicken", "static/recipe2.jpg"),
       # model.Recipe(3, user, "Panetone", "static/recipe3.jpg")"""   
    return render_template("main/index.html") 

@bp.route("/profile")
def profile():
   # user = model.User(name = "Mary", password = "1234", email = "mary@example.com")
    return render_template("main/profile.html")

@bp.route("/create_recipe")
def create_recipe():
    return render_template("main/create_recipe.html")

@bp.route("/recipe1")
def recipe():
    """Esto es solo un ejemplo de como se vería una receta, pero hay que ver como hacer para que cuando se de click a una, se 
    forme la vista"""
   # r = model.Recipe(user_id = 1, title = "Gingerbread Cookies", main_photo = "static/recipe1.jpg", 
  #  description = "Delicius cookies for doing on christmas", cooking_time = 40, n_person = 4, dificulty = "Easy", 
   #                  quantified_ingredients = ["5 Eggs", "500 gr Flour", "Ginger", "50 gr Sugar"], steps = ["Beat the eggs", "Take a spoon", "Turn on the oven", "Decorate"])
    return render_template("main/recipe.html")

