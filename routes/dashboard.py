from app import app, render_template, session, url_for, redirect


@app.route('/')
@app.route('/admin')
def admin():
    if not ('is_login' in session):
        return redirect('/login')
    module = 'dashboard'
    return render_template("admin/dashboard.html", module=module)
