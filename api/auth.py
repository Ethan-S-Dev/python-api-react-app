import os
import json
import random
import requests
import jwt

from base64 import b64encode
from dotenv import load_dotenv, find_dotenv
from flask import Flask,Response,jsonify,render_template,templating

load_dotenv(find_dotenv())


JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

app = Flask(__name__)


@app.route("/",defaults={"path":""})
@app.route("/<path:path>")
def catch_all(path):
    data = {"Message": "Hello Frome Python API!"}
    resp = Response(data,
    status=200,
    mimetype="application/json")

    return resp

if __name__ == "__main__":
    app.run(debug=True)


