from app import app, render_template, request, jsonify
from helpers import db_config
from sqlalchemy import text
from routes.category import getCategoryList
from routes.product import getProductList
from datetime import datetime


@app.route('/pos')
def pos():
    return render_template("pos/pos.html")


@app.get('/pos/get-data')
def getData():
    category_list = getCategoryList()
    product_list = getProductList()
    return {
        'category_list': getCategoryList(),
        'product_list': getProductList()
    }


@app.post('/pos/payment')
def payment():
    form = request.get_json()
    selected_product = form['selected_product']
    total_amount = form['total_amount']
    received_amount = form['received_amount']
    # insert data to sale table
    cnn = db_config.connection()
    result = cnn.execute(text(f"""
            INSERT INTO `sale`
            VALUES
                (
                    NULL,
                    'ref_code_123',
                    '{datetime.now()}',
                    '{total_amount}',
                    '{received_amount}',
                    '1'
                )
    	"""))
    last_sale_id = result.lastrowid

    # loop insert data to sale_item
    for item in selected_product:
        print(item['id'])
        sale_item = cnn.execute(text(f"""
                INSERT INTO `sale_item`
                VALUES
                    (
                        NULL,
                        '{last_sale_id}',
                        '{item['id']}',
                        '{item['qty']}',
                        '{item['price']}',
                        '{float(item['qty']) * float(item['price'])}'
                    )
        	"""))

    cnn.commit()
    cnn.close()
    return {'status': "success"}
