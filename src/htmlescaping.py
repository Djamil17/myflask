from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# run http://127.0.0.1:5000/foo and you will get "hello, foo!"
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
