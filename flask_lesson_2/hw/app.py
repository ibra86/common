from flask import Flask, render_template

from routes.products.products_route import products

app = Flask(__name__)
app.register_blueprint(products)

import os

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

root_dir = os.path.join(app.root_path)

all_products = []

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", var_list=['Products', 'Supermarkets'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('err_404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
