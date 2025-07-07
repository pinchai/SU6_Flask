from flask import Flask, render_template, jsonify
import requests
app = Flask(__name__)


@app.get("/")
@app.get("/home")
def home():
    product_list = []
    api_url = 'https://fakestoreapi.com/products'
    r = requests.get(api_url)
    if r.status_code == 200:
        product_list = r.json()
    return render_template('home.html', product_list=product_list)


@app.get('/about')
def about():
    return render_template('about.html')


@app.get('/contact')
def contact():
    return render_template('contact.html')


@app.get('/api/products')
def products():
    product = [
        {
            'id': 1,
            'name': 'coca',
            'category': 'drink',
            'cost': '0.25',
            'price': '0.5',
            'image': '/static/coca.jpeg',
        }
    ]
    return jsonify(product)
