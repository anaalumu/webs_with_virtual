from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt

from . import model

bp = Blueprint("auth", __name__)

@bp.route("/userlogin")
def login():
    return render_template("auth/login.html")

@bp.route("/userlogin", methods=["POST"] )
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

   #check the user with that email 
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
      #correct password  
        flash("Welcome!")
        return redirect(url_for("main.index"))
    else:
        flash("Invalid email or password. Please try again.")
        return redirect(url_for("auth.login"))





@bp.route("/signup")
def signup():
    return render_template("auth/signup.html")


@bp.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    # Check that passwords are equal
    if password != request.form.get("password_repeat"):
        flash("Sorry, passwords are different")
        return redirect(url_for("auth.signup"))
        
    # Check if the email is already at the database
    query = db.select(model.User).where(model.User.email == email)
    user = db.session.execute(query).scalar_one_or_none()
    if user:
        flash("Sorry, the email you provided is already registered")
        return redirect(url_for("auth.signup"))
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = model.User(email=email, name=username, password=password_hash)
    db.session.add(new_user)
    db.session.commit()

    flash("You've successfully signed up!")
    return redirect(url_for("main.index"))