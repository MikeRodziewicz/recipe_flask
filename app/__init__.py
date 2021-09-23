# here is where I combine all the imports and return the app

import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

# Each blueprint has to be registered here with the app itself, so the same goes for auth, but also for any other packages i have. 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
