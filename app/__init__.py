import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app


from app import models













# from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail
# from flask_login import LoginManager
# from config import config


# bootstrap = Bootstrap()
# moment = Moment()
# db = SQLAlchemy()
# mail = Mail()

# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'

# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(config[config_name])
#     config[config_name].init_app(app)

#     bootstrap.init_app(app)
#     moment.init_app(app)
#     mail.init_app(app)
#     db.init_app(app)
#     login_manager.init_app(app)
 
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint, url_prefix='/auth')

#     return app