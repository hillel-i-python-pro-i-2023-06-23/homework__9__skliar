from flask import Flask, render_template, request
from app.services.create_table import create_table
from app.services.read_all_table import table_read_all
from app.services.add_table_string import add_user
from app.services.read_table_string import read_row

from pathlib import Path

current_dir = Path(__file__).parent
app = Flask(__name__, template_folder=current_dir.parent / "templates")


@app.route("/")
def main():
    return "hello"


@app.route("/all")
def read_all():
    return table_read_all()


@app.route("/add", methods=["GET", "POST"])
def add_users():
    if request.method == "POST":
        add_user()
    return render_template("index.html")


@app.route("/choose", methods=["GET", "POST"])
def find_users():
    if request.method == "POST":
        phone_ID_to_find = request.form["ID"]
        user = read_row(phone_ID_to_find)
        if user is not None:
            return render_template("choose.html", user=user)
        else:
            return render_template("choose.html", error_message="Рядок с указанным ID не найден")

    return render_template("choose.html")


create_table()
