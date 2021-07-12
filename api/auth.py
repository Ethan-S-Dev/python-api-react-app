from flask import Flask ,Response

app = Flask(__name__)

app.add_url_rule("/api/auth",endpoint="index")

@app.endpoint("index")
def index():
    return Response({"Message":"Hey"},status=200,content_type="application/json")

if __name__ == "__main__":
    app.run(debug=True)