from flask import Flask, session
from flask import render_template, redirect, url_for, request
import sqlite3
import hashlib

name = 'main'

app = Flask(name)
app.secret_key = 'Niveau'

def get_db_connection():
    conn = sqlite3.connect('Database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
  return redirect(url_for('admin_login'))

@app.route('/adm_login', methods=['GET', 'POST'])
def admin_login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        global gUsername
        gUsername = username
        conn.close()

        if user and user['password'] == hashed_password:
            session['user_id'] = user['id']
            return redirect(url_for('admin_panel'))
        else:
            error = 'Неправильное имя пользователя или пароль'

    return render_template('Login page.html', error=error)

@app.route('/admin_panel')
def admin_panel():
    return render_template('Admin panel.html', username=gUsername)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if name == 'main':
  app.run(debug=True)
