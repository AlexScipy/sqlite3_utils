import sqlite3
from datetime import datetime


# import db


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
    cursor.execute(f"SELECT * FROM accounts")  # accounts è il nome specifico della tabella
    rows = cursor.fetchall()
    cursor.close()
    return rows  # mi ritorna una lista di tuple,
    # dove ogni tupla è un elemento della tabella del db"""


def update_user(connection, username, old_password, new_password):
    cursor = connection.cursor()
    condition = cursor.execute(f'''
                    SELECT 
                        CASE
                            WHEN EXISTS (
                                SELECT 1
                                FROM accounts
                                WHERE username = ? AND password_ = ?
                            )
                            THEN TRUE
                            ELSE FALSE
                        END AS account_exists;
                    ''', (username, old_password)).fetchone()[0]

    # print(condition)
    connection.commit()
    try:
        if condition:
            cursor.execute(f"SELECT id FROM accounts WHERE username = ?", (username,))
            id_ = cursor.fetchone()[0]
            cursor.execute(f"UPDATE accounts SET password_ = ?, updated_at = ? WHERE id = ?",
                           (new_password, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id_))
            connection.commit()
            return f"Password of {username} successfully updated!\n"
        else:
            return "you are not allowed!", 500
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


def remove_user(connection, username, password):
    # verifico che lo username di input sia presente nel db
    cursor = connection.cursor()
    username_db = cursor.execute(f"SELECT FROM accounts WHERE username = {username}")
    password_db = cursor.execute(f"SELECT FROM accounts WHERE password_ = {password}")
    # if username == username_db and password == password_db:
    try:
        cursor.execute(f"DELETE FROM accounts WHERE username = ?", (username,))
        connection.commit()
        return f"User removed with Success!\n"
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")


#if __name__ == "__main__":
    #db = Database("database.db")
    #print(update_user(db.connect(), "andrea", "abcde4", "1234"))
