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
    return User(name=data['user_name'], gender=data['gender'], email=data['email'], image=data['image'])

@app.route('/user_add', methods=['POST'])
def IsUserExists():
    global dataBase
    if not request.json or not check_data(request.json):
        return jsonify('{"result" : bad arguments}')
    data = request.json
    status = dataBase.add_user(get_user_from_data(data))
    
    print(status)
    return jsonify('{"result" : ' + f'status = {status}')


# def normalize_data(value):
#     nvalue = list(value)
#     nvalue[0] = f'\'{nvalue[0]}\''
#     nvalue[1] = f'\'{nvalue[1]}\''
#     nvalue[2] = f'\'{nvalue[2]}\''
#     nvalue[3] = f'\'{nvalue[3]}\''
#     nvalue[4] = f'\'{nvalue[4]}\''
#     print('(' + ", ".join(nvalue) + ')')
#     return '(' + ", ".join(nvalue) + ')'


# @app.route('/get_user_info/<string:username>', methods=['GET'])
# def get_courier_by_id(username):
#     DB_new = connect('NewMessages.sqlite3')
#     new_messages = GET(DB_new, query)
#     query = "DELETE FROM messages WHERE from_username == " + f'"{username}"' + \
#             " OR to_username == " + f'"{username}"'
#     SET(DB_new, query)
#     DB_new.close()

#     new_messages = list(map(normalize_data, new_messages))

#     DB_old = connect('OldMessages.sqlite3')
#     query = "INSERT INTO messages VALUES "
#     for value in new_messages:
#         print(query + value)
#         SET(DB_old, query + value)
#     DB_old.close()
#     print('NEW:', new_messages)
#     data = dict()
#     data['new_messages'] = new_messages

#     return jsonify(data)


if __name__ == '__main__':
    dataBase = BotDB(path='./db/data.db', create_table=False)
    app.run(host='0.0.0.0', port=8080)


'''
curl -i -H "Content-Type: application/json" -X GET\
-d '{"data": [
    {
    "email": "evzman2002@mail.ru",
    "password": "OPN1INU2002"
    }
    ]}' http://0.0.0.0:8080/Users
    

curl -i -H "Content-Type: application/json" -X GET\
    -d '{
    "email" : "evzman2002@mail.ru",
    "password" : "OPN1INU2002"
    }' http://0.0.0.0:8080/Users
'''