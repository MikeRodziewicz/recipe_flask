
from flask import render_template, session, flash
from flask.helpers import url_for
from werkzeug.utils import redirect
from .forms import UserForm, IngredientForm, ContainerForm
from . import main
from app.models import User, Ingredient, Container
from app import db
from ..mail import sending_email


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
            flash('Your email has been added.')
            sending_email()
        else:
            session['know'] = True
            flash('Your email aready exists.')
        session['email'] = form.email.data
        form.email.data = ''
        return redirect(url_for('main.index'))
    return render_template('user.html', form=form,
    email = session.get('email'), known=session.get('known', False))


@main.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    form = IngredientForm()
    if not form.validate_on_submit():
        return render_template('ingredient.html', form=form)
    ingredient = Ingredient(
        name = form.ingredient_name.data,
        quantity = form.quantity.data,
        container = Container.query.get(form.container_id.data)
    )
    with db.session() as session:
        session.add(ingredient)
        session.commit()
    return redirect(url_for('main.index'))


@main.route('/add_container', methods=['GET', 'POST'])
def add_container():
    form = ContainerForm()
    if not form.validate_on_submit():
        return render_template('container.html', form=form)
    container = Container(
        name = form.container_name.data,
        capacity = form.capacity.data
    )
    with db.session() as session:
        session.add(container)
        session.commit()
    return redirect(url_for('main.index'))