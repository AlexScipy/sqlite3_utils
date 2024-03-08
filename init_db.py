import sqlite3, codecs

connection = sqlite3.connect('database.db')
with codecs.open('database.sql', encoding='utf-8') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()