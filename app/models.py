from werkzeug.security import generate_password_hash, check_password_hash
from enum import unique
from operator import contains, index
from flask_login import UserMixin, AnonymousUserMixin
from flask import current_app, request, url_for
from sqlalchemy.orm import backref
from app import db, login



#TODO password management to be added here
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self) -> str:
        return f'This is the user e-mail {self.email}'

    @property
    def password(self):
        raise AttributeError('you cannot read password')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
           return (self.user_id)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Container(db.Model):
    container_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True)
    capacity = db.Column(db.Integer)
    ingredient = db.relationship('Ingredient', backref='container', lazy='dynamic')


class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True)
    quantity = db.Column(db.Integer)
    container_id = db.Column(db.Integer, db.ForeignKey('container.container_id'))

