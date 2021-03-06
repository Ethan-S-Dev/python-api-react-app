import os
import jwt
import json
from dotenv import find_dotenv,load_dotenv
from flask import Flask ,Response,jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

load_dotenv(find_dotenv())

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

class HelloWorld(Resource):
    def get(self):
        return jsonify({"message":"Hello World!"})

class Multi(Resource):
    def get(self,num):
        return jsonify({'result':num*10})

class Secret(Resource):
    def get(self):
        return jsonify({'secret':JWT_SECRET_KEY})



api.add_resource(HelloWorld,"/api/auth")
api.add_resource(Multi,"/api/auth/multi/<int:num>")
api.add_resource(Secret,"/api/auth/secret")

if __name__ == "__main__":
    app.run(debug=True)