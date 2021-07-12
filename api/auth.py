import os
import jwt
import json
from dotenv import find_dotenv,load_dotenv
from flask import Flask ,Response


load_dotenv(find_dotenv())

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


app = Flask(__name__)




@app.route("/api/auth")
def index():
    data = json.dumps({"Message":"Hey"})
    return Response(data,status=200,content_type="application/json")

@app.route("/api/auth/secret")
def secret():
    data = json.dumps({"Secret":JWT_SECRET_KEY})
    return Response(data,status=200,content_type="application/json")

    
if __name__ == "__main__":
    app.run(debug=True)