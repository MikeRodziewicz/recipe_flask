from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo 

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

