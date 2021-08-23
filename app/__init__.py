import os
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'supersecretkey'

  bootstrap.init_app(app)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
