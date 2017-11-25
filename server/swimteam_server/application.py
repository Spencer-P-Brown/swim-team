
import inspect, os, sys

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.routing import BaseConverter
import flask_restless

from sqlalchemy import Table, Column, Integer, String, VARCHAR, LargeBinary, UnicodeText

from swimteam_server.extensions import DB
# from swimteam_server.models import models
from swimteam_server.blueprints.users import generate_users_blueprint

MIGRATE = Migrate()


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]



class User(DB.Model):

    __tablename__ = "users"

    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(250), nullable=False, unique=True)
    password = DB.Column(DB.String(250), nullable=False)


def generate_application(config=None):
    """Generate an application from a given configuration file."""
    application = Flask(__name__)
    application.config.from_object(config or 'swimteam_server.config.dev')
    CORS(application, send_wildcard=True)
    application.url_map.converters['regex'] = RegexConverter
    application.register_blueprint(generate_users_blueprint(application.config))

    # create db instance
    DB.app = application
    DB.init_app(application)
    application.db = DB
    DB.create_all()

    # flask_restless
    STANDARD_METHODS = ['GET', 'POST', 'PUT', 'DELETE']
    results_per_page = -1 # turn off pagination
    manager = flask_restless.APIManager(application, flask_sqlalchemy_db=DB)
    # https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
    # TODO: fix this
    # clsmembers = inspect.getmembers(sys.modules['vehicles.models.models'], inspect.isclass)
    # for cls_tuple in clsmembers:
    #     klass = cls_tuple[1]
    #     # check if is sqlalchemy class
    #     if hasattr(klass, '__tablename__'):
    #         manager.create_api(klass, methods=STANDARD_METHODS, results_per_page=results_per_page)

    # hardcode for now
    # manager.create_api(User, methods=STANDARD_METHODS, results_per_page=results_per_page)
    manager.create_api(User, methods=STANDARD_METHODS)

    MIGRATE.init_app(application, DB)
    return application


def generate_test_application(config=None):
    """Generate a test application from a given configuration file."""
    application = Flask(__name__)
    application.config.from_object(config or 'swimteam_server.config.test')
    CORS(application, send_wildcard=True)
    return application
