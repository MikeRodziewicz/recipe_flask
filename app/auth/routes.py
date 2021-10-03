from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data): # where does the check_password() come from
            flash(_('Incorrect password or email')) # why do we use _ here?
            return redirect(url_for('auth.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', form=form)
        

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))



#TODO register form to be created
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.pass_1.data)
        db.session.add(user)
        db.session.commit()
        flash('you are registered')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

