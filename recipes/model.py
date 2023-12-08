from . import db
import flask_login

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    recipes = db.relationship('Recipes', back_populates='user')
    ratings = db.relationship('Rating', back_populates='user')
    bookmarks = db.relationship('Bookmarks', back_populates='user')
    photos = db.relationship('Photos', back_populates='user')

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    main_photo = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    n_person = db.Column(db.Integer, nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    dificulty = db.Column(db.String(50), nullable=False)
    user = db.relationship('User', back_populates='recipes')
    quantified_ingredients = db.relationship('QuantifiedIngredients', back_populates='recipes')
    steps = db.relationship('Steps', back_populates='recipes')
    ratings = db.relationship('Rating', back_populates='recipes')
    bookmarks = db.relationship('Bookmarks', back_populates='recipes')
    photos = db.relationship('Photos', back_populates='recipes')

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    quantified_ingredients = db.relationship('QuantifiedIngredients', back_populates='ingredients')

class QuantifiedIngredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    unit_measurement = db.Column(db.String(10), nullable=False)
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable=False)
    recipes_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    ingredients = db.relationship('Ingredients', back_populates='quantified_ingredients')
    recipes = db.relationship('Recipes', back_populates='quantified_ingredients')

class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    sequence_number = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipes = db.relationship('Recipes', back_populates='steps')

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    user = db.relationship('User', back_populates='ratings')
    recipes = db.relationship('Recipes', back_populates='ratings')

class Bookmarks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    recipes = db.relationship('Recipes', back_populates='bookmarks')
    user = db.relationship('User', back_populates='bookmarks')

class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    file_extension = db.Column(db.String(10), nullable=False)
    user = db.relationship('User', back_populates='photos')
    recipes = db.relationship('Recipes', back_populates='photos')
    


"""class User:
    def __init__(self, user_id, email, name):
        self.user_id = user_id
        self.email = email
        self.name = name

class Recipe:
    def __init__(self, recipe_id, user, title, photo, description, cooking_time, n_persons, dificulty, ingredients, steps, other_photos):
        self.recipe_id = recipe_id
        self.user = user
        self.title = title
        self.photo = photo
        self.description = description
        self.cooking_time = cooking_time
        self.n_persons = n_persons
        self.dificulty = dificulty
        self.ingredients = ingredients
        self.steps = steps
        self.other_photos = other_photos"""
