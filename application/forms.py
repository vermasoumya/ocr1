from wtforms import TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    text_field = TextAreaField("Data", validators=[DataRequired()])