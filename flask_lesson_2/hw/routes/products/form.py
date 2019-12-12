from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, FloatField
from wtforms import validators


class AddProductForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    description = StringField('Description', validators=[validators.DataRequired()])
    price = FloatField('Price', validators=[validators.DataRequired()])
    image_file = FileField('Load image',
                           validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
