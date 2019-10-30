from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables():
	var_list = ['beans', 'carrot', 'beetroot', 'cucumber']
	return render_template('vegetables.html', var_list=var_list)



@app.route('/fruits')
def fruits():
	var_list=['melon', 'apple', 'strawberry', 'grape']
	return render_template('fruits.html', var_list=var_list)


if __name__ == '__main__':
    app.run(debug=True)
