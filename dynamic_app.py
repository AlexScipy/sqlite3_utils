from flask import Flask, request, jsonify
from util_db import *

app = Flask(__name__)
db = Database("database.db")
#usernames = [usr[1] for usr in get_data_from_db_table(db.connect())]
#all_passwords_from_db = [psw[3] for psw in get_data_from_db_table(db.connect())]



@app.route("/home", methods=['GET'])
def hello():
    return "<h1>hello</h1>"


@app.route('/insert_user', methods=['POST'])
def handle_insert_user():
    try:
        #table_name = request.json['table_name']
        username = request.json['username']
        #email = request.json['email']
        #password = request.json['password']
        return insert_user(db.connect(), username)
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/get_users', methods=['GET'])
def handle_get_users():
    try:
        #table_name = request.json['table_name']
        return jsonify(get_data_from_db_table(db.connect()))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/remove_user', methods=['DELETE'])
def handle_remove_user():
    try:
        username = request.json['username']
        password = request.json['password']
        #usernames = [usr[1] for usr in get_data_from_db_table(db.connect())]
        return remove_user(db.connect(), username, password)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/update_user', methods=['PUT'])
def handle_update_user():
    try:
        username = request.json['username']
        old_password = request.json['old_password']
        new_password = request.json['new_password']
        return update_user(db.connect(), username, old_password, new_password)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
