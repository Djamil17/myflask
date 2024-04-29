from flask import Flask, request, render_template

app = Flask(__name__)


def valid_login(username: str, password: str): 
    if username.islower():
        return True
    if len(password) > 5:
        return True
 

def log_the_user_in(username: str):
    print("username")


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)