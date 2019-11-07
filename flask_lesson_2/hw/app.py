from flask import Flask, render_template

from routes.products_route import products

app = Flask(__name__)
app.register_blueprint(products)


@app.route('/')
@app.route('/home')
def home():
    var_list = []
    print(var_list)
    return render_template("home.html", var_list=var_list)


if __name__ == '__main__':
    app.run(debug=True)
