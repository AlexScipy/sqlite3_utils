from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from datetime import datetime

#app = Flask(__name__)

def connect(db):
    connection = sqlite3.connect(db)                                        # Inizializzo connection con la connessione sqlite3 al db;
    connection.row_factory = sqlite3.Row                                    # Imposto la connessione su Row in modo da poter utilizzare...
    return connection                                                       # ...le chiavi dei campi anziché gli indici per accedere ai valori;

def get_data_from_db_table(db, table_name):
    connection = connect(db)                                                # Connessione al db richiamando la funzione connect();
    cursor = connection.cursor()                                            # Inizializzo un cursore sulla connessione al db;
    cursor.execute(f"SELECT * FROM {table_name}")                           # Eseguo una query SQL per selezionare la tabella x;
    rows = cursor.fetchall()                                                # Inizializzo su rows tutte le righe della tabella selezionata sopra con fetchall();
    accounts = []                                                           # Creo una lista vuota da popolare in seguito con le righe della tabella del db;
    for id_, username, email, psw, create_date, update_date in rows:            # Sapendo che il la tabella ha 6 campi, ciclo nelle righe della tabella,
        accounts.append([id_, username, email, psw, create_date, update_date])  # popolando la lista accounts[] con i valori dei 6 campi per ogni riga;
    cursor.close()                                                          # chiudo il cursore;
    connection.close()                                                      # chiudo la connessione al db;
    return accounts                                                         # ritorno la lista di righe della tabella del db;

def insert_user(db, table_name):
    username = input(f"username: ")
    email = input("email: ")
    password = input("password: ")
    create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:                                                                    # dentro un try-except;
        connection = connect(db)                                            # mi connetto al db;
        #cursor = connection.cursor()
        connection.execute(f"INSERT INTO {table_name} (username, email, password_, created_at, updated_at) VALUES (?, ?, ?, ?, ?)", # eseguo la insert
                           (username, email, password, create_date, update_date))
        connection.commit()                                                 # faccio il commit() per salvare l'operazione fatta;
        connection.close()                                                  # chiudo la connessione;
        return "Insert done!\n"                                             # stampa di debug in caso di successo;
    except Exception as e:
        raise ValueError(f"Error occurred: {e}\n")                          # stampa di debug in caso di eccezzione;

def remove_user(db, table_name):
    user_id = input("Insert the user 'id' to remove: ")
    found = False
    for el in get_data_from_db_table(db, table_name):
        if int(user_id) == el[0]:
            try:
                conncetion = connect(db)
                conncetion.execute(f"DELETE FROM {table_name} WHERE id = {user_id}")
                conncetion.commit()
                conncetion.close()
                found = True
            except Exception as e:
                raise ValueError(f"Error occurred: {e}\n")
    if found:
        return f"User id= {user_id} removed from table= {table_name}!\n"
    else:
        return f"id not in {table_name}\n"



#============================= TESTS ====================================================================================

#print(insert_user("database.db", "accounts"))
#print("###################################################\n")
#print(get_data_from_db_table("database.db", "accounts"))
#print("###################################################\n")
#print(remove_user("database.db", "accounts"))

"""@app.route("/")
def index():
    return render_template("signup.html")

app.route("/stampa_db")
def print_db(db):
    connection = connect(db)


@app.route("/signup", methods=("GET", "POST"))
def signup():
    return redirect("/homepage")


if __name__ == '__main':
    app.run()"""