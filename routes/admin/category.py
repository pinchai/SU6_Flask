from app import app
from flask import render_template


@app.get("/admin/category")
def category():
    return render_template('admin/category/index.html', module='category')
