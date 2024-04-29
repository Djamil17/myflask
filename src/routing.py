from flask import Flask

app = Flask(__name__)


# run http://127.0.0.1:5000 to get index page 
@app.route('/')
def index():
    return 'Index Page'


# run in browser http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    return 'Hello, World'