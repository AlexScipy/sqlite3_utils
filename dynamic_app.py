from flask import Flask, request, jsonify
from util_db import Database, get_data_from_db_table, update_user, insert_user, remove_user

app = Flask(__name__)
db = Database("database.db")


@app.route("/home", methods=['GET'])
def hello():
    return "<h1>hello</h1>"


@app.route('/insert_user', methods=['POST'])
def handle_insert_user():
    try:
        table_name = request.json['table_name']
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        return insert_user(db.connect(), table_name, username, email, password)
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
        table_name = request.json['table_name']
        user_id = request.json['user_id']
        return remove_user(db.connect(), table_name, user_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/update_user', methods=['PUT'])
def handle_update_user():
    try:
        table_name = request.json['table_name']
        username = request.json['username']
        password = request.json['old_password']
        new_password = request.json['new_password']
        # verifico che la password vecchia inserita sia la stessa presente nel db
        all_passwords_from_db = [psw[3] for psw in get_data_from_db_table(db.connect(), table_name)]
        print(all_passwords_from_db)
        if password in all_passwords_from_db:
            return update_user(db.connect(), table_name, username, new_password)
        else:
            return jsonify({'error': "password not matched in the db..."})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
