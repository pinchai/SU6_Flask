from app import app
from flask import render_template


@app.get("/admin/category")
def category_index():
    return render_template('admin/category/index.html', module='category')


@app.get("/admin/category/list")
def category_list():
    categories = get_category_list()
    return categories


def get_category_list():
    return [
        {'id': 1, 'name': 'Electronics'},
        {'id': 2, 'name': 'Books'},
        {'id': 3, 'name': 'Clothing'},
        {'id': 3, 'name': 'Home & Kitchen'},
        {'id': 3, 'name': 'Sports & Outdoors'},
    ]
