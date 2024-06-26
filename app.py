from flask import Flask, render_template, request, redirect, url_for
import os

UPLOAD_FOLDER = 'image'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    return render_template("index.html", student_list=student_list)


@app.get('/product')
def product():
    return render_template('product.html', product_list=product_list)


@app.get('/product_detail')
def product_detail():
    product_id = request.args.get('id')
    current_product = []
    for item in product_list:
        if item['id'] == product_id:
            current_product = item

    return render_template('product_detail.html', current_product=current_product)


@app.get('/checkout')
def checkout():
    product_id = request.args.get('id')
    current_product = []
    for item in product_list:
        if item['id'] == product_id:
            current_product = item

    return render_template('checkout.html', current_product=current_product)


@app.post('/submit_order')
def submit_order():
    product_id = request.form.get('product_id')
    current_product = []
    for item in product_list:
        if item['id'] == product_id:
            current_product = item

    name = request.form.get('fullname')
    phone = request.form.get('phone')
    email = request.form.get('email')

    return current_product


@app.get('/about')
def about():
    return render_template("about.html")


@app.get('/contact')
def contact():
    return render_template("contact.html")


@app.get('/jinja')
def jinja():
    return render_template('jinja.html')


@app.get('/add_product')
def add_product():
    return render_template('add_product.html')


@app.post('/submit_new_product')
def submit_new_product():
    product_id = request.form.get('product_id')
    file = request.files['file']
    title = request.form.get('title')
    price = request.form.get('price')
    category = request.form.get('category')
    description = request.form.get('description')

    # Option 1
    # file.save('/image', f.filename)
    # Option 2
    file.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/product', file.filename))

    return redirect(url_for('add_product', name=file.filename))


if __name__ == '__main__':
    app.run()
