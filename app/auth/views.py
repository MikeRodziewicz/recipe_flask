from app import auth
from flask import render_template, session, url_for, redirect
from .forms import LoginForm, RegistrationForm
from . import auth

#TODO login form to be created
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)

#TODO register form to be created
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

#TODO add User profile page use user.html file for that
