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

@views.route("/delete-note", methods=["POST"])
def delete_note():
  note = json.loads(request.data)
  note_id = note["id"]
  note_to_delete = Note.query.get(note_id)
  if note:
    if note_to_delete.user_id == current_user.id:
      db.session.delete(note_to_delete)
      db.session.commit()

  return jsonify({})

@views.route("/edit-note", methods=["GET", "POST"])
def edit_note():
  # if request.method == "POST":
  #   note = json.loads(request.data)
    # note_id = note["id"]
    # note_to_update = Note.query.get(note_id)
    # if note_to_update.user_id == current_user.id:
    #   db.session.delete(note_to_update)
    #   db.session.commit()

  return render_template("edit-note.html", user=current_user)