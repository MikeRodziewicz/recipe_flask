
from flask import render_template
from .forms import NameForm
from . import main


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