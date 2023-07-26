from app.services.db_connection import DBConnection


def read_row(phone_ID_to_find):
    with DBConnection() as connection:
        user = connection.execute("SELECT * FROM phones WHERE phone_ID = ?", (phone_ID_to_find,)).fetchone()
    return user
