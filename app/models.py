from enum import unique
from operator import index
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, index=True)

    def __repr__(self) -> str:
        return f'This is the user e-mail {self.email}'

