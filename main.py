# here is where I actually execcute the creation of the app, pass the ENV var to the function and have the app running. 
import os
import click
from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Ingredient, Container


app = create_app()
migration = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Ingredient=Ingredient,
                Container=Container)