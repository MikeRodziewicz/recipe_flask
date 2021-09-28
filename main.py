import os
from app import create_app, db
from flask_migrate import Migrate, upgrade
from app.models import User, Ingredient, Container


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Ingredient=Ingredient,
                Container=Container)