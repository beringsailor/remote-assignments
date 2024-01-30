import json
from flask import (Flask, request, render_template, 
                   redirect, url_for, make_response)

app = Flask(__name__)
app.secret_key = '@IKUH$@*OHJDS98y9dd9pw;s9dso'

# Assignment-1
@app.route("/")
def hello():
    return "Hello, My Server!"


# Assignment-2
@app.route('/data', methods=["GET"])
def add_func():
    try:
        num = request.args.get('number')
        if num == None:
            return "Lack of Parameter"
        else:
            num = int(num)
            result = 0
            for item in range(num+1):
                result += item
            return str(result)
    except (ValueError,TypeError):
        return "Wrong Parameter"


# Assignment-3
@app.route("/sum.html", methods=["GET"])
def sum():
    return render_template('sum.html')


# Assignment-4
def get_saved_data():
    try:
        username = json.loads(request.cookies.get('userID'))
    except TypeError:
        username = {}
    return username

@app.route('/trackName')
def new():
    username = get_saved_data()
    if 'userID' in request.cookies:
        return (redirect('/myName'))
    return render_template('index.html')

@app.route('/save', methods = ['POST'])
def save():
    response = make_response(redirect(url_for('new')))
    username = get_saved_data()
    username.update(dict(request.form.items()))
    response.set_cookie('userID', json.dumps(username))
    return response

@app.route("/myName")
def index():
    username = get_saved_data()
    if 'userID' in request.cookies:
        return '<h1> Welcome, username: ' + username['name']  + '</h1>'
    else:
        return redirect(url_for('new'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
