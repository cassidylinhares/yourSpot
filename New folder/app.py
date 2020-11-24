from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__, template_folder='views')
app.secret_key = "my precious"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'project0'

# Intialize MySQL
mysql = MySQL(app)
@app.route('/')
def home():
    if 'logged_in' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
        return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password,))

        user = cursor.fetchone()
        # If account exists in accounts table in out database
        if user:
            # Create session data, we can access this data in other routes
            session['logged_in'] = True
            session['id'] = user['id']
            session['username'] = user['username']

            return 'logged in finally'
        else:
            msg = 'No user in file'
            #flash('Logged in bro!')
            #return redirect(url_for('welcome'))
    return render_template('login.html', msg=msg)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access

        Fname = request.form['first_name']
        Lname = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

         # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE username = %s', (username,))
        user = cursor.fetchone()
        # If account exists show error and validation checks
        if user:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s, %s, %s, %s)', (Fname, Lname, username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg)

@app.route('/out')
def success():
        return render_template('success.html')
@app.route('/logout')
def logout():
        session.pop('logged_in', None)
        session.pop('id', None)
        session.pop('username', None)
        flash('Logged out!')
        return redirect(url_for('login'))


if __name__ == '__main__':
        app.run(debug=True)
