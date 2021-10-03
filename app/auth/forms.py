from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError 
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    pass_1 = PasswordField('Password', validators=[DataRequired(), 
    EqualTo('pass_2', message='Passwords do not match.')])
    pass_2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_if_user_already_exists(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email has already been used')

