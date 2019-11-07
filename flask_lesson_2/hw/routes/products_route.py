from flask import Blueprint, render_template, request

products = Blueprint('products', __name__, template_folder='templates')

all_products = []


@products.route('/products', methods=['GET'])
def get_all_products():
    data = all_products
    return render_template('all_products.html', data=data)


@products.route('/products', methods=['POST'])
def add_product():
    all_products.append(request.json)
    print(request.data)
    print(request.json)
    return "ok"
