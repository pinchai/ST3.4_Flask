from app import app, render_template
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
