from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    email = StringField('what is your e-mail?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class IngredientForm(FlaskForm):
    pass