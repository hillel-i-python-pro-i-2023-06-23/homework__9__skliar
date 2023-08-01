from flask import Flask, render_template, request, Response
from app.services.create_table import create_table
from app.services.read_all_table import table_read_all
from app.services.add_table_string import add_user
from app.services.read_table_string import read_row
from app.services.db_connection import DBConnection

from pathlib import Path

current_dir = Path(__file__).parent
app = Flask(__name__, template_folder=current_dir.parent / "templates")


@app.route("/")
def main():
    return "hello   /all    /add      /choose     /update     /delete"


@app.route("/all")
def read_all():
    return table_read_all()


@app.route("/add", methods=["GET", "POST"])
def add_users():
    if request.method == "POST":
        contact_name = request.form["name"]
        phone_value = int(request.form["phone_value"])
        add_user(contact_name, phone_value)
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


@app.route("/update", methods=["GET", "POST"])
def update_user():
    if request.method == "POST":
        phone_ID_to_update = request.form["ID"]
        update_name = request.form["name_update"]
        update_telephone = request.form["telephone_update"]

        if not update_name and not update_telephone:
            return Response(
                "Надо хотя бы один парамерт",
                status=400,
            )

        with DBConnection() as connection:
            if not update_name:
                result = connection.execute(
                    "SELECT contact_name FROM phones WHERE phone_ID = ?", (phone_ID_to_update,)
                ).fetchone()
                if result:
                    update_name = result["contact_name"]
                else:
                    return Response(
                        "Запись с указанным phone_ID не найдена",
                        status=404,
                    )

            if not update_telephone:
                result = connection.execute(
                    "SELECT phone_value FROM phones WHERE phone_ID = ?", (phone_ID_to_update,)
                ).fetchone()
                if result:
                    update_telephone = result["phone_value"]
                else:
                    return Response(
                        "Запись с указанным phone_ID не найдена",
                        status=404,
                    )

            connection.execute(
                "UPDATE phones SET contact_name = ?, phone_value = ? WHERE phone_ID = ?",
                (update_name, update_telephone, phone_ID_to_update),
            )
            connection.commit()

    return render_template("update.html")


@app.route("/delete", methods=["POST", "GET"])
def delete_string():
    status = None
    if request.method == "POST":
        delete_ID = request.form["ID"]

        with DBConnection() as connection:
            with connection:
                result = connection.execute("SELECT * FROM phones WHERE phone_ID = ?", (delete_ID,)).fetchone()
                if result:
                    connection.execute(
                        "DELETE FROM phones WHERE phone_ID = ?",
                        (delete_ID),
                    )
                    status = "удалено"
                else:
                    status = "Запись с указанным phone_ID не найдена"

    return render_template("delete.html", status=status)


create_table()
