from re import sub
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from . import main


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@main.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@main.route('/secret', methods=['GET', 'POST'])
def secret():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data  = ''
    return render_template('secret.html', form=form, name=name)