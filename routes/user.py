from app import app, render_template, request
from helpers import db_config
from sqlalchemy import text


@app.route('/admin/user')
def user():
    module = "user"
    return render_template("admin/user.html", module=module)


@app.get('/admin/get-user')
def getUser():
    # Test the connection
    result = db_config.connection().execute(text("SELECT * FROM user"))
    data = result.fetchall()
    user_list = []
    for item in data:
        user_list.append(
            {
                'id': item[0],
                'name': item[1],
                'gender': item[2],
                'phone': item[3],
                'email': item[4],
                'role': item[5],
                'address': item[6],
            }
        )

    return user_list


@app.post('/admin/create-user')
def createUser():
    json_data = request.get_json()
    name = json_data['name']
    gender = json_data['gender']
    phone = json_data['phone']
    email = json_data['email']
    role = json_data['role']
    address = json_data['address']
    cnn = db_config.connection()
    result = cnn.execute(text(f"""
        INSERT INTO `user`
        VALUES
            (
                NULL,
                '{name}',
                '{gender}',
                '{phone}',
                '{email}',
                '{role}',
                '{address}'
            )
	"""))
    cnn.commit()
    cnn.close()
    return f"{result}"


@app.post('/admin/update-user')
def updateUser():
    json_data = request.get_json()
    user_id = json_data['id']
    name = json_data['name']
    gender = json_data['gender']
    phone = json_data['phone']
    email = json_data['email']
    role = json_data['role']
    address = json_data['address']
    cnn = db_config.connection()
    result = cnn.execute(text(f"""
    UPDATE `user` 
    SET `name` = '{name}',
    gender = '{gender}',
    phone = '{phone}',
    email = '{email}',
    role = '{role}',
    address = '{address}' 
    WHERE
        `id` = '{user_id}'
	"""))
    cnn.commit()
    cnn.close()
    return f"{result}"

@app.post('/admin/delete-user')
def deleteUser():
    json_data = request.get_json()
    user_id = json_data['user_id']
    cnn = db_config.connection()
    result = cnn.execute(text(f"""DELETE FROM `user` WHERE `id` = {user_id}"""))
    cnn.commit()
    cnn.close()
    return f"{result}"

