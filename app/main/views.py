
from flask import render_template, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from .forms import NameForm, UserForm
from . import main
from app.models import User
from app import db


@main.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@main.route('/secret', methods=['GET', 'POST'])
def secret():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data  = ''
    return render_template('secret.html', form=form, name=name)


@main.route('/user', methods=['GET', 'POST'])
def user():
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['know'] = True
        session['email'] = form.email.data
        form.email.data = ''
        return redirect(url_for('main.index'))
    return render_template('user.html', form=form,
    email = session.get('email'), known=session.get('known', False))
