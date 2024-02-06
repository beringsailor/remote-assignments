from flask import (Flask, render_template, session,
                   request, redirect, url_for)
import pymysql
import re

app = Flask(__name__)
app.secret_key = '*&G*%RF^YGHJ' 

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'assignment'
app.config['MYSQL_HOST'] = 'localhost'

# Connect to the database
mysql = pymysql.connect(
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB'],
    host=app.config['MYSQL_HOST'],
    cursorclass=pymysql.cursors.DictCursor
)

# http://localhost:3000/ this will be home page
@app.route('/home', methods=['GET','POST'])
def signin():
    mysql.commit()
    cursor = mysql.cursor(pymysql.cursors.DictCursor)
    
    msg = ''
    if request.method == 'POST' and request.args.get("s") == "in" and 'email' in request.form and 'password' in request.form:
        
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM user WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()

        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            session['password'] = account['password']
            return redirect(url_for('member'))
        else: 
            msg = "Incorrect email or password!"

    elif request.method == 'POST' and request.args.get("s") == "up" and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO user VALUES (%s, %s)', (email, password)) 
            mysql.commit()
            return redirect(url_for('member'))
            
    return render_template('index.html', msg=msg)


@app.route("/member")
def member():
    msg="Welcome, our prestigious member."
    return render_template('member.html', msg = msg)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

# @app.route('/test')
# def testdb():
#     try:
#         with mysql.cursor() as cursor:
#             cursor.execute("SELECT 1")
#             result = cursor.fetchall()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         return f'<h1>Something is broken. Error: {e}</h1>'
    
# ref: https://tutorial101.blogspot.com/2020/02/login-register-sytem-with-python-flask.html


