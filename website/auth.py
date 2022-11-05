from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
  if request.method == "POST":
    email = request.form.get("email")
    first_name = request.form.get("firstName")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    user = User.query.filter_by(email=email).first()

    if user:
      flash("Email already exists.", category="error")
    if len(first_name) < 2:
      flash("First name can not be smaller than 2 characters.", category="error")
    elif password1 != password2:
      flash("Passwords do not match.", category="error")
    elif len(password1) < 4:
      flash("Password can not be smaller than 4 characters.", category="error")
    else:
      new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="SHA256"))
      db.session.add(new_user)
      db.session.commit()

      flash("User created successfully!", category="success")
      return redirect(url_for("views.home"))

  return render_template("sign-up.html")

@auth.route("/sign-in", methods=["GET", "POST"])
def sign_in():
  return render_template("sign-in.html")