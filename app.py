from flask import Flask, render_template, \
    request, redirect, url_for, jsonify, session, flash
from functools import wraps
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/image'


@app.get('/login')
def login():
    session.pop('auth', None)
    session.pop('is_login', None)
    return render_template('auth/login.html')


@app.post('/do_login')
def doLogin():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123':
        session['auth'] = {
            'username': 'admin',
            'role': 'admin',
            'profile': 'profile.png'
        }
        session['is_login'] = True
        return redirect('/admin')
    else:
        flash('Invalid username or password!', 'danger')
        return redirect('/login')


@app.get('/logout')
def logout():
    if not ('is_login' in session):
        return redirect('/login')

    session.pop('auth', None)
    session.pop('is_login', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


import routes


if __name__ == '__main__':
    app.run(port=5050)
