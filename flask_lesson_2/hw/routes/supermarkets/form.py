from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms import validators


class AddSupermarketForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    location = StringField('Description', validators=[validators.DataRequired()])
    image_file = FileField('Load image',
                           validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
