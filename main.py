from flask import Flask, jsonify, abort
import sqlite3
from sqlite3 import Error
from flask import make_response, request
from datetime import datetime
from db.dbschema import User
from db.bot_db import BotDB


app = Flask(__name__)
required_fields = [
    'user_name', 'gender', 'image', 'email'
]

def check_data(data):
    for f in required_fields:
        if f not in data:
            return 0
    return 1

def get_user_from_data(data):
    return User(user_name=data['user_name'], gender=data['gender'], email=data['email'], image=data['image'].encode())

@app.route('/user_add', methods=['POST'])
def user_add():
    global dataBase
    print(request.json)
    print('======================================')
    if not request.json or not check_data(request.json):
        return jsonify('{"result" : bad arguments}')
    data = request.json
    status = dataBase.add_user(get_user_from_data(data))
    
    print(status)
    return jsonify('{"result" : OK}')

@app.route('/user_update', methods=['POST'])
def user_update():
    global dataBase
    print(request.json)
    print('======================================')
    if not request.json or not check_data(request.json):
        return jsonify('{"result" : bad arguments}')
    data = request.json
    status = dataBase.update_user(get_user_from_data(data))
    
    print(status)
    return jsonify('{"result": OK}')


@app.route('/get_user_info/<string:username>', methods=['GET'])
def get_user_info(username):
    global dataBase
    print('username:', username)
    user = dataBase.get_user(username)
    print(user)
    return jsonify('{"result": ' + str(user) + '}')

@app.route('/user_delete/<string:username>', methods=['POST'])
def user_delete(username):
    global dataBase
    print('username:', username)
    users = dataBase.delete_user(username)
    print(users)
    return jsonify('{"result": OK}')

@app.route('/get_all_users_info', methods=['GET'])
def get_all_users_info():
    global dataBase
    users = dataBase.show_all_users()
    return jsonify('{"result": ' + str(users) + '}')


if __name__ == '__main__':
    dataBase = BotDB(path='./db/data.db', create_table=False)
    app.run(host='0.0.0.0', port=8080)


'''
curl -i -H "Content-Type: application/json" -X POST\
-d '{
    "user_name": "yan",
    "email": "evzman2002@mail.ru",
    "image": "OPN1INU2002",
    "gender": "male"
    }' http://0.0.0.0:8080/user_add

curl http://0.0.0.0:8080/get_user_info/yan
'''