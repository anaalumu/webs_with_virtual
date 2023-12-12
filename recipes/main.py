from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user
from . import db
from sqlalchemy import func, desc, nullslast

from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    best_rated_recipes = db.session.query(
        model.Recipes.id,
        model.Recipes.title,
        model.User.id.label('user_id'),
        model.User.name.label('user'),
        model.Recipes.main_photo
    ) \
    .join(model.User) \
    .join(model.Rating) \
    .group_by(model.Recipes.id, model.Recipes.title, model.User.name, model.Recipes.main_photo) \
    .order_by(func.avg(model.Rating.value).desc()) \
    .limit(6) \
    .all()
    
    return render_template("main/index.html", recipes=best_rated_recipes)

@bp.route("/profile/<int:user_id>")
def profile(user_id):
    user = model.User.query.get(user_id)
    return render_template("main/profile.html", user = user)

@bp.route("/all_recipes")
def all_recipes():
    recetas = model.Recipes.query.all()
    return render_template('main/all_recipes.html', recetas=recetas)

@bp.route('/sort_recipes/<criteria>')
def sort_recipes(criteria):
    if criteria == 'title':
        sorted_recipes = model.Recipes.query.order_by(model.Recipes.title).all()
    elif criteria == 'rating':
        sorted_recipes = model.Recipes.query.outerjoin(model.Rating).group_by(model.Recipes.id).order_by(desc(db.func.avg(model.Rating.value))).all()
    elif criteria == 'dificulty':
        sorted_recipes = model.Recipes.query.order_by(db.case((model.Recipes.dificulty == 'easy', 1),(model.Recipes.dificulty == 'medium', 2),(model.Recipes.dificulty == 'hard', 3),(model.Recipes.dificulty == 'expert', 4),else_=5)).all()
    else:
        sorted_recipes = model.Recipes.query.all()

    #JSON formmat
    serialized_recipes = [
        {
            'id': recipe.id,
            'title': recipe.title,
            'user': {'name': recipe.user.name},
            'main_photo': recipe.main_photo
        }
        for recipe in sorted_recipes
    ]

    return jsonify({'recipes': serialized_recipes})


