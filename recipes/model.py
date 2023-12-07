
class User:
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
        self.other_photos = other_photos
