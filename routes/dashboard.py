from app import app, render_template


@app.route('/admin')
def admin():
    module = 'dashboard'
    return render_template("admin/dashboard.html", module=module)
