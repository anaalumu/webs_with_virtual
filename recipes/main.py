from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from . import db
from sqlalchemy import func
from sqlalchemy.orm import joinedload

from . import model

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    best_rated_recipes = db.session.query(
        model.Recipes.id,
        model.Recipes.title,
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


