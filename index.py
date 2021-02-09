import jwt
import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
app = Flask(__name__)

load_dotenv()
app.config['MONGO_URI']=os.getenv('DB_CONNECT')

mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacto')
def conctacto():
    return render_template('contacto.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/notificaciones')
def notification():
    return render_template('notifications.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/new_contacto',methods=['POST'])
def new_contacto():
    name = request.json['name']
    email = request.json['email']
    info = request.json['info']

    if name !="" and email !="" and info:
        id = mongo.db.clientes.insert_one(
            {'nombre':name,'email':email,'informacion_adicional':info}
        )
        response = {
            'id':str(id),
            'status':'complete'
        }
        return jsonify(response)
    else:
        return jsonify({'status':'error 500'})
    
@app.route('/user_api')
def user_api():
    return render_template('user_api.html')

from client_api import Tokens, db_actions
import hashlib
@app.route('/new_user_api', methods=['POST'])
def new_user_api():
    name = request.json['name']
    email = request.json['email']
    pwd = str(request.json['password'])
    pwd = pwd.encode()
    h_pwd = hashlib.sha224(pwd).hexdigest()

    token  = Tokens.generate_token(name,email,h_pwd)
    url_token = Tokens.url_token()
    data = {'name':name,'email':email,'token':token,'url_token':url_token, 'password':h_pwd}
    res = db_actions.user_save(mongo,data)
    if res !="error":
        return jsonify({'status':'successfull', 'token':token, 'url_token':url_token})
    else:
        return jsonify({'status': 'error 500', 'message': 'Error while insert into DB'})

if __name__ == '__main__':
    app.run(debug=True)