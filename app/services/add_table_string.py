from app.services.db_connection import DBConnection
from flask import request


def add_user():
    if request.method == "POST":
        contact_name = request.form["name"]
        phone_value = int(request.form["phone_value"])
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (?, ?)",
                (contact_name, phone_value),
            )
