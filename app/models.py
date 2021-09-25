from enum import unique
from operator import contains, index
from sqlalchemy.orm import backref
from . import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, index=True)

    def __repr__(self) -> str:
        return f'This is the user e-mail {self.email}'


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



