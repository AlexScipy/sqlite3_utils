import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db):
        self.db = db

    def connect(self):
        connection = sqlite3.connect(self.db)  # Inizializzo connection con la connessione sqlite3 al db;
        connection.row_factory = sqlite3.Row  # Imposto la connessione su Row in modo da poter utilizzare...
        return connection

    def cursor(self):
        return self.connect().cursor()

    def commit(self):
        return self.connect().commit()

    def close(self):
        self.connect().close()


def get_tables(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") # query per ottenere i nomi di tutte le tabelle presenti nel database SQLite.
    tables = cursor.fetchall()
    cursor.close()
    print("Tables Avaible:")
    return [table[0] for table in tables]  # Ritorna una lista contenente solo i nomi delle tabelle


def get_data_from_db_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    cursor.close()
    return [list(row) for row in rows]


def insert_user(connection, table_name):
    username = input("username: ")
    email = input("email: ")
    password = input("password: ")
    create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (username, email, password_, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (username, email, password, create_date, update_date))
        connection.commit()
        return "Insert done!\n"
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")


def remove_user(connection, table_name):
    user_id = input("Insert the user 'id' to remove: ")
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (user_id,))
        connection.commit()
        return f"User id = {user_id} removed from table = {table_name}!\n"
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")


if __name__ == "__main__":
    db_file = input("INSERT DATABASE FILENAME: ")
    db = Database(db_file)
    connection = db.connect()

    while True:
        # Definisci un menu interattivo
        print("\nMenu:")
        print("1. Insert User")
        print("2. Get Users")
        print("3. Remove User")
        print("4. Exit")
        choice = input("Select an option (1/2/3/4): ")

        if choice == "1":
            print(get_tables(connection))
            table_name = input("INSERT TABLE NAME: ")
            print(insert_user(connection, table_name))
        elif choice == "2":
            print(get_tables(connection))
            table_name = input("INSERT TABLE NAME: ")
            print(get_data_from_db_table(connection, table_name))
        elif choice == "3":
            print(get_tables(connection))
            table_name = input("INSERT TABLE NAME: ")
            print(remove_user(connection, table_name))
        elif choice.lower() == "4" or choice.lower() == "exit":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

    connection.close()
