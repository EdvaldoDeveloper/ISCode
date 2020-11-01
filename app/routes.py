from flask import render_template, request, redirect, url_for
from app import db

from app.models import Contact


def init_app(app):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            contact = Contact()
            contact.name = request.form["name"]
            contact.email = request.form["email"]
            contact.telephone = request.form["telephone"]
            contact.subject = request.form["subject"]
            contact.message = request.form["message"]

            db.session.add(contact)
            db.session.commit()

            return redirect(url_for("home"))

        return render_template("index.html")
