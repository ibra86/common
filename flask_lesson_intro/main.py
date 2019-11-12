from flask import Flask, render_template

from flask_lesson_intro.utils import get_data

app = Flask(__name__)

data = get_data()
entity_list = [d.get('title') for d in data]


@app.route('/')
def get_home_page():
    return render_template("home.html", entity_list=entity_list)


@app.route('/<entity>')
def get_entity_page(entity):
    entity_description = [d.get('text') for d in data for k, v in d.items() if (
            k == 'title' and v.lower().replace(' ', '-') == entity)]
    entity_description = next(iter(entity_description), None)
    return render_template("entity.html", entity=entity, entity_description=entity_description, entity_list=entity_list)


if __name__ == "__main__":
    app.run(debug=True)
