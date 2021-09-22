from flask import render_template
from . import main

@main.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@main.route('/secret', methods=['GET'])
def secret():
  return render_template('secret.html')