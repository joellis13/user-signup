from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_signup():
    return render_template('signup_form.html')

@app.route('/signup', methods=['post'])
def signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
        
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if not username or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "That's not a valid username"
        username = ''
    
    if not password:
        password_error = "That's not a valid password"
        password = ''

    if not verify or password != verify:
        verify_error = "Passwords don't match"
        verify = ''

    if not email:
        pass
    elif not email or len(email) < 3 or len(email) > 20 or ' ' in email or '@' not in email or '.' not in email:
        email_error = "That's not a valid email"
        email = ''
    
    if not username_error and not password_error and not verify_error and not email_error:
        welcome_msg = "Welcome, " + username + "!"
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup_form.html',
        username=username,
        username_error=username_error,
        password=password,
        password_error=password_error,
        verify=verify,
        verify_error=verify_error,
        email=email,
        email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return '<h1>Wecome, {0}!</h1>'.format(username)

app.run()