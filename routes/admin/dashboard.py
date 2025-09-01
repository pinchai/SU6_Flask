from app import app
from flask import render_template


@app.get("/admin")
@app.get("/admin/dashboard")
def dashboard():
    return render_template('admin/dashboard/index.html', module='dashboard')
