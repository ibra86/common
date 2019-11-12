import os

from flask import Blueprint, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename

from db import all_supermarkets
from model import Supermarket
from .form import AddSupermarketForm

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates', static_folder='static',
                         static_url_path='/routes/supermarkets/static')

save_img_dir = os.path.join('routes', 'supermarkets', 'static', 'img')
os.makedirs(save_img_dir, exist_ok=True)


@supermarkets.route('/supermarket')
def get_all_supermarkets():
    return render_template('all_supermarkets.html', var_list=all_supermarkets)


@supermarkets.route('/supermarket', methods=['POST'])
def post_add_supermarket():
    form = AddSupermarketForm()

    if form.validate_on_submit():
        id__ = max(all_supermarkets, key=lambda x: x.get('id_'), default={}).get('id_', 0) + 1
        supermarket_obj = Supermarket(id__, form.name.data, form.location.data,
                                      secure_filename(form.image_file.data.filename))

        all_supermarkets.append(supermarket_obj.__dict__)
        f = form.image_file.data
        f.save(os.path.join(save_img_dir, secure_filename(f.filename)))

        return redirect(url_for('supermarkets.get_all_supermarkets'))
    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/add-supermarket')
def get_add_supermarket():
    form = AddSupermarketForm()
    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/supermarket/<int:id_>')
def get_supermarket(id_):
    var_list = [p for p in all_supermarkets if p.get('id_') == id_]
    sess_supermarket_id = str(var_list[0].get('id_'))
    session[sess_supermarket_id] = True
    return render_template('all_supermarkets.html', var_list=var_list)
