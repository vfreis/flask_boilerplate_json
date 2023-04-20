import os
from flask import Flask
from .env import mysql_var
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    
    from .models import Usuario, Agenda
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'''{mysql_var['driver']}://{mysql_var['host']}:{mysql_var['port']}/{mysql_var['database']}'''
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_HOST}'
    app.config['SECRET_KEY'] = mysql_var['secret_key']
    
    db.init_app(app)

    with app.app_context():
        db.create_all()
    # create_database(app)

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    # a simple page that says hello
    @app.route('/')
    def start():
        return 'On'

    return app

def create_database(app):
    db.create_all(app)