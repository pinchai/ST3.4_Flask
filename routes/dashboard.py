from app import app, render_template


@app.route('/admin')
def admin():
    return render_template("admin/starter.html")
