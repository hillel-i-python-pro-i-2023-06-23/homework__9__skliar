from app.services.db_connection import DBConnection


def table_read_all():
    with DBConnection() as connection:
        users_phones = connection.execute("SELECT * FROM phones").fetchall()

    return "<br>".join(
        [
            f'{user["phone_ID"]}:'
            f' {user["contact_name"]} number is {user["phone_value"]}'
            for user in users_phones
        ]
    )
