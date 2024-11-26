from flask import Flask, render_template, \
    request, redirect, url_for, jsonify
import os
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/image'

conn = sqlite3.connect('database.db', check_same_thread=False)

product_list = [
    {
        'id': '1',
        'title': 'night cream',
        'price': '20',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",
        'image': 'product1.jpg'
    },
    {
        'id': '2',
        'title': 'day cream',
        'price': '25',
        'description': "Some quick example text to build on the card title and make up the bulk of the card's content.",
        'image': 'product2.jpg'
    }
]


import routes


@app.route('/')
@app.route('/home')
def home():
    student_list = [
        {
            'id': '001',
            'name': 'dara',
            'gender': 'male',
            'GPA': '4.0',
        },
        {
            'id': '002',
            'name': 'rithy',
            'gender': 'male',
            'GPA': '3.0',
        }
    ]
    return render_template("index.html", student_list=student_list, module='home')


if __name__ == '__main__':
    app.run()
