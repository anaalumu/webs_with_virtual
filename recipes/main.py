import datetime
import dateutil.tz

from flask import Blueprint, render_template


from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    user = model.User(1, "mary@example.com", "mary")
    recipes =[ model.Recipe(1, user, "Gingerbread Cookies", "static/recipe1.jpg", 
    "Delicius cookies for doing on christmas", 40, 4, "Easy", 
                     ["5 Eggs", "500 gr Flour", "Ginger", "50 gr Sugar"], 
                     ["Beat the eggs", "Take a spoon", "Turn on the oven", "Decorate"], 
                     ["static/ou1", "static/ou2"])] 
       # model.Recipe(2, user, "Stuffed Chicken", "static/recipe2.jpg"),
       # model.Recipe(3, user, "Panetone", "static/recipe3.jpg")   
    return render_template("main/index.html", recipes = recipes)

@bp.route("/profile")
def profile():
    user = model.User(1, "mary@example.com", "mary")
    return render_template("main/profile.html", user = user)

@bp.route("/userlogin")
def userlogin():
    return render_template("main/userlogin.html")

@bp.route("/userregister")
def userregister():
    return render_template("main/userregister.html")

@bp.route("/create_recipe")
def create_recipe():
    return render_template("main/create_recipe.html")

@bp.route("/recipe1")
def recipe():
    """Esto es solo un ejemplo de como se vería una receta, pero hay que ver como hacer para que cuando se de click a una, se 
    forme la vista"""
    user = model.User(1, "mary@example.com", "mary")
    r = model.Recipe(1, user, "Gingerbread Cookies", "static/recipe1.jpg", "Delicius cookies for doing on christmas", 40, 4, "Easy", 
                     ["5 Eggs", "500 gr Flour", "Ginger", "50 gr Sugar"], ["Beat the eggs", "Take a spoon", "Turn on the oven", "Decorate"], 
                     ["static/ou1.jpg", "static/ou2.jpeg"])
    return render_template("main/recipe.html", recipe = r)

