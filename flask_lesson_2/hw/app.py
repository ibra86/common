import os

from flask import Flask, render_template

from routes.products.route import products
from routes.supermarkets.route import supermarkets

app = Flask(__name__)

app.register_blueprint(products)
app.register_blueprint(supermarkets)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", var_list=['Products', 'Supermarkets'])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('err_404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
