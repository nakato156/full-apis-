import os
from dotenv import load_dotenv
import jwt
import secrets
load_dotenv()
secret = os.getenv('SECRET')
class Tokens():
    def generate_token(name, email, password):
        try:
            payload = {"exp":60*60*8, "name": name , "email":email, "password": password}
            token = jwt.encode(payload, secret, algorithm='HS256')
            return token
        except Exception as e:
            return 'Error'

    def url_token():
        url_token = secrets.token_urlsafe(20)
        return url_token

    def decode_token(_token):
        try:
            token = jwt.decode(_token,secret,options={'verify_exp':False},algorithms=['HS256'])
            if token:
                return token
            else:
                return 'error decode token'
        except jwt.ExpiredSignatureError:
            return 'TOKEN expired'
        except jwt.InvalidTokenError:
            return 'Token invalid'

class db_actions():
    def user_save(BD,data):
        try:
            id = BD.db.clientes_api.insert_one(data)
            return id
        except Exception as e:
            return 'error'
            
