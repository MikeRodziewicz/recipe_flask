from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
from ..models import Container
from flask_wtf.form import _Auto

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    email = StringField('what is your e-mail?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


class ContainerForm(FlaskForm):
    container_name = StringField('Name the container', validators=[DataRequired()])
    capacity = StringField('What is the capacity?', validators=[DataRequired()])

class IngredientForm(FlaskForm):

    ingredient_name = StringField('Name the ingredient', validators=[DataRequired()])
    quantity = StringField('How many items to add?', validators=[DataRequired()])
    container_id = SelectField('Container', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')
   
    def __init__(self, formdata=_Auto, **kwargs):
            super(IngredientForm, self).__init__(**kwargs)
            self.container_id.choices = [(container_id.container_id, container_id.name) for container_id in Container.query.order_by(Container.name).all()]
          
    
 