import os

from flask import Blueprint, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename

from db import all_products
from model import Product
from .form import AddProductForm

products = Blueprint('products', __name__, template_folder='templates', static_folder='static',
                     static_url_path='/routes/products/static')

save_img_dir = os.path.join('routes', 'products', 'static', 'img')
os.makedirs(save_img_dir, exist_ok=True)


@products.route('/product')
def get_all_products():
    return render_template('all_products.html', var_list=all_products)


@products.route('/product', methods=['POST'])
def post_add_product():
    form = AddProductForm()

    if form.validate_on_submit():
        id__ = max(all_products, key=lambda x: x.get('id_'), default={}).get('id_', 0) + 1
        product_obj = Product(id__, form.name.data, form.description.data, form.price.data,
                              secure_filename(form.image_file.data.filename))

        all_products.append(product_obj.__dict__)
        f = form.image_file.data
        f.save(os.path.join(save_img_dir, secure_filename(f.filename)))

        return redirect(url_for('products.get_all_products'))
    return render_template('add_product.html', form=form)


@products.route('/add-product')
def get_add_product():
    form = AddProductForm()
    return render_template('add_product.html', form=form)


@products.route('/product/<int:id_>')
def get_product(id_):
    var_list = [p for p in all_products if p.get('id_') == id_]
    sess_product_id = str(var_list[0].get('id_'))
    session[sess_product_id] = True
    return render_template('all_products.html', var_list=var_list)
