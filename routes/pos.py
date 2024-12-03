from app import app, render_template, request, jsonify
from helpers import db_config
from sqlalchemy import text
from routes.category import getCategoryList
from routes.product import getProductList


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

