from flask import Flask, render_template, request
from app.services.create_table import create_table
from app.services.read_all_table import table_read_all
from app.services.add_table_string import add_user

from pathlib import Path

current_dir = Path(__file__).parent
app = Flask(__name__, template_folder=current_dir / "../templates")


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


create_table()
