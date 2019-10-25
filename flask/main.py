from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    vegetables_tmpl = 'vegetables.html'
    fruits_tmpl = 'fruits.html'
    return render_template('home.html')#, vegetables_tmpl, fruits_tmpl)


@app.route('/vegetables')
def vegetables(vars=['beans', 'carrot', 'beetroot', 'cucumber']):
    return render_template('vegetables.html', vars=vars)


@app.route('/fruits')
def fruits(vars=['melon', 'apple', 'strawberry', 'grape']):
    return render_template('fruits.html', vars=vars)


if __name__ == '__main__':
    app.run(debug=True)
