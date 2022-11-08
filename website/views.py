from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import current_user, login_required
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
  if request.method == "POST":
    note = request.form.get("note")
    new_note = Note(text=note, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for("views.home"))

  return render_template("home.html", user=current_user)

@views.route("/delete-note-<int:id>")
def delete_note(id):
  note_to_delete = Note.query.get(id)
  if id:
    if note_to_delete.user_id == current_user.id:
      db.session.delete(note_to_delete)
      db.session.commit()
      return redirect(url_for("views.home"))



@views.route("/edit-note-<int:id>", methods=["GET", "POST"])
def edit_note(id):
  note = Note.query.get(id)

  if request.method == "POST":
    new_note = request.form.get("new_note")
    print(db.engine.execute(f'UPDATE Note SET text="{new_note}" WHERE id="{id}"'))
    return redirect(url_for("views.home"))

  return render_template("edit-note.html", user=current_user, current_note_text=note.text)