from app import app, render_template, request
from helpers import db_config
from sqlalchemy import text


@app.route('/admin/category')
def category():
    module = "category"
    return render_template("admin/category.html", module=module)


@app.get('/admin/get-category')
def getCategory():
    # Test the connection
    result = db_config.connection().execute(text("SELECT * FROM category"))
    data = result.fetchall()
    category_list = []
    for item in data:
        category_list.append(
            {
                'id': item[0],
                'name': item[1],
                'description': item[2],
            }
        )

    return category_list


@app.post('/admin/create-category')
def createCategory():
    json_data = request.get_json()
    name = json_data['name']
    description = json_data['description']
    cnn = db_config.connection()
    result = cnn.execute(text(f"""
        INSERT INTO `category`
        VALUES
            (
                NULL,
                '{name}',
                '{description}'
            )
	"""))
    cnn.commit()
    return f"{result}"


@app.post('/admin/update-category')
def updateCategory():
    json_data = request.get_json()
    category_id = json_data['id']
    name = json_data['name']
    description = json_data['description']

    cnn = db_config.connection()
    result = cnn.execute(text(f"""
    UPDATE `category` 
    SET `name` = '{name}',
    `description` = '{description}'
    WHERE
        `id` = '{category_id}'
	"""))
    cnn.commit()
    return f"{result}"

@app.post('/admin/delete-category')
def deleteCategory():
    json_data = request.get_json()
    category_id = json_data['category_id']
    cnn = db_config.connection()
    result = cnn.execute(text(f"""DELETE FROM `category` WHERE `id` = {category_id}"""))
    cnn.commit()
    return f"{result}"

