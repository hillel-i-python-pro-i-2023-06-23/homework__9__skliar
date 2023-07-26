from app.services.db_connection import DBConnection


def add_user(contact_name, phone_value):
    with DBConnection() as connection:
        with connection:
            connection.execute(
                "INSERT INTO phones (contact_name, phone_value) VALUES (?, ?)",
                (contact_name, phone_value),
            )
