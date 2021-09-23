from app import auth
from flask import render_template, session, url_for, redirect
from .forms import LoginForm, RegistrationForm
from . import auth

# @main.route('/secret', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)
