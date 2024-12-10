from app import app, render_template, request, jsonify
from helpers import db_config
from sqlalchemy import text
from routes.category import getCategoryList


@app.route('/admin/product')
def product():
    module = "product"
    return render_template("admin/product.html", module=module)


@app.get('/admin/get-product')
def getProduct():
    category_list = getCategoryList()
    product_list = getProductList()

    return {'category_list': getCategoryList(), 'product_list': getProductList()}
    # return category_list


@app.post('/admin/create-product')
def createProduct():
    json_data = request.get_json()
    name = json_data['name']
    cost = json_data['cost']
    price = json_data['price']
    category_id = json_data['category_id']
    description = json_data['description']

    cnn = db_config.connection()
    result = cnn.execute(text(f"""
        INSERT INTO `product`
        VALUES
            (
                NULL,
                '{name}',
                '{category_id}',
                '{cost}',
                '{price}',
                '{description}'
            )
	"""))
    cnn.commit()
    cnn.close()
    return f"{result}"


@app.post('/admin/update-product')
def updateProduct():
    json_data = request.get_json()
    product_id = json_data['id']
    name = json_data['name']
    cost = json_data['cost']
    price = json_data['price']
    category_id = json_data['category_id']
    description = json_data['description']

    cnn = db_config.connection()
    result = cnn.execute(text(f"""
    UPDATE `product` 
    SET `name` = '{name}',
    `description` = '{description}',
    `cost` = '{cost}',
    `price` = '{price}',
    `category_id` = '{category_id}'
    WHERE
        `id` = '{product_id}'
	"""))
    cnn.commit()
    cnn.close()
    return f"{result}"

@app.post('/admin/delete-product')
def deleteProduct():
    json_data = request.get_json()
    product_id = json_data['product_id']
    cnn = db_config.connection()
    result = cnn.execute(text(f"""DELETE FROM `product` WHERE `id` = {product_id}"""))
    cnn.commit()
    cnn.close()
    return f"{result}"


def getProductList():
    # Test the connection
    cnn = db_config.connection()
    result = cnn.execute(
        text("""
                    SELECT
                product.id,
                product.`name`,
                product.`cost`,
                product.`price`,
                product.`description`,
                category.id as category_id,
                category.name as category_name
            FROM
                product
                INNER JOIN category ON product.category_id = category.id
        """)
    )
    data = result.fetchall()
    cnn.close()
    product_list = []
    for item in data:
        product_list.append(
            {
                'id': item[0],
                'name': item[1],
                'cost': item[2],
                'price': item[3],
                'description': item[4],
                'category_id': item[5],
                'category_name': item[6],
            }
        )
    return product_list

