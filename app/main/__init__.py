# I register the blueprint here, take the routes from views module and then they can be used by the app

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

