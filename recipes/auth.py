from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db, bcrypt
import flask_login
from flask_login import current_user
from flask_login import logout_user

from . import model

bp = Blueprint("auth", __name__)

@bp.route("/logout")
def logout():
    return render_template("auth/logout.html")

@bp.route("/logout", methods=["POST"] )
def logout_post():
    logout_user()  
    return redirect(url_for('auth.userlogin')) 


@bp.route("/userlogin")
def userlogin():
    return render_template("auth/userlogin.html")

@bp.route("/userlogin", methods=["POST"] )
def userlogin_post():
    email = request.form.get("email")
    password = request.form.get("password")

   #check the user with that email 
    user = model.User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password):
      #correct password  
        flash("Welcome!")
        flask_login.login_user(user)
        return redirect(url_for("main.index"))
    else:
        flash("Invalid email or password. Please try again.")
        return redirect(url_for("auth.userlogin"))


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
    return redirect(url_for("auth.userlogin"))