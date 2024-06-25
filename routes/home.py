from app import app, render_template
import sqlite3


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.get('/about')
def about():
    return render_template("about.html")


@app.get('/contact')
def contact():
    return render_template("contact.html")
