from app import app
from flask import render_template, jsonify, request


@app.get("/")
@app.get("/home")
def home():
    from product import products
    product_list = products
    # api_url = 'https://fakestoreapi.com/products'
    # r = requests.get(api_url)
    # if r.status_code == 200:
    #     product_list = r.json()
    return render_template('home.html', product_list=product_list)


@app.get("/product-detail")
def product_detail():
    from product import products, getByID
    pro_id = request.args.get('pro_id', type=int)
    product = getByID(pro_id)
    # api_url = f"https://fakestoreapi.com/products/{pro_id}"
    # r = requests.get(api_url)
    # if r.status_code == 200:
    #     product = r.json()
    # print(product)

    return render_template('product_detail.html', product=product)


@app.get('/cart')
def cart():
    return render_template('cart.html')


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
