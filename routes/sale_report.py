from app import app, render_template, request, jsonify, session, redirect
from helpers import db_config
from sqlalchemy import text


@app.route('/admin/sale_report')
def saleReport():
    if not ('is_login' in session):
        return redirect('/login')
    module = "sale_report"
    return render_template("admin/sale_report.html", module=module)


@app.get('/admin/get_sale_report')
def getSaleReport():
    cnn = db_config.connection()
    result = cnn.execute(
        text("""SELECT * FROM sale""")
    )
    data = result.fetchall()
    cnn.close()
    product_list = []
    for item in data:
        product_list.append(
            {
                'id': item[0],
                'ref_code': item[1],
                'date_time': item[2],
                'total_amount': item[3],
                'received_amount': item[4],
                'user': 'admin',
            }
        )
    return product_list

