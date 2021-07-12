print("strat")
import os
import json
import random
import requests
print("badimports")
import jwt

from base64 import b64encode
from dotenv import load_dotenv, find_dotenv
from flask import Flask,Response,jsonify,render_template,templating

print("dotenv")
load_dotenv(find_dotenv())

print("os")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
print("flask")
app = Flask(__name__)

print("route")
@app.route("/",defaults={"path":""})
@app.route("/<path:path>")
def catch_all(path):
    data = {"Message": "Hello Frome Python API!","secret":JWT_SECRET_KEY}
    resp = Response(data,
    status=200,
    mimetype="application/json")

    return resp
print("--main--")
if __name__ == "__main__":
    app.run(debug=True)


