import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db):
        self.db = db

    def connect(self):
        return sqlite3.connect(self.db)

    def cursor(self, connection):
        return connection.cursor()

    def commit(self, connection):
        connection.commit()

    def close(self, connection):
        connection.close()


def get_data_from_db_table(connection):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM accounts") #accounts è il nome specifico della tabella
    rows = cursor.fetchall()
    cursor.close()
    return [list(row) for row in rows]


def update_user(connection, table_name, username, new_password):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT id FROM {table_name} WHERE username = ?", (username,))
        id_ = cursor.fetchone()[0]
        cursor.execute(f"UPDATE {table_name} SET password_ = ?, updated_at = ? WHERE id = ?",
                       (new_password, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_))
        connection.commit()
        return f"Password of {username} successfully updated!\n"
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")


def insert_user(connection, table_name, username, email, password):
    try:
        create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (username, email, password_, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (username, email, password, create_date, create_date))
        connection.commit()
        return "Insert done!\n"
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")


def remove_user(connection, table_name, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (user_id,))
        connection.commit()
        return f"User id = {user_id} removed from table = {table_name}!\n"
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")

