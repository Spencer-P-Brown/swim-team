
import inspect, os, sys

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.routing import BaseConverter
import flask_restless

from swimteam_server.extensions import DB
# from swimteam_server.models import models

MIGRATE = Migrate()


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def generate_application(config=None):
    """Generate an application from a given configuration file."""
    application = Flask(__name__)
    application.config.from_object(config or 'swimteam_server.config.dev')
    CORS(application, send_wildcard=True)
    application.url_map.converters['regex'] = RegexConverter
    # application.register_blueprint(blueprint_file.generate_blueprint_callback(application.config))

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
    # manager.create_api(models.Location, methods=STANDARD_METHODS, results_per_page=results_per_page)

    MIGRATE.init_app(application, DB)
    return application


def generate_test_application(config=None):
    """Generate a test application from a given configuration file."""
    application = Flask(__name__)
    application.config.from_object(config or 'swimteam_server.config.test')
    CORS(application, send_wildcard=True)
    return application
