# here is where I combine all the imports and return the app

import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

bootstrap = Bootstrap()
moment = Moment()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'supersecretkey'

  bootstrap.init_app(app)
  moment.init_app(app)


# Each blueprint has to be registered here with the app itself, so the same goes for auth, but also for any other packages i have. 
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
