from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField("Search for an Item", validators=[DataRequired()])
    submit = SubmitField("Search")
