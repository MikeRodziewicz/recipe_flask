import unittest
from flask import current_app
from app import create_app, db
from app.models import User

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password = 'test')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'test')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_check(self):
        u = User(password = 'test')
        self.assertTrue(u.verify_password('test'))
        self.assertFalse(u.verify_password('spam'))

    def test_password_salt(self):
        u1 = User(password = 'test')
        u2 = User(password = 'test')
        self.assertTrue(u1.password_hash != u2.password_hash)

    