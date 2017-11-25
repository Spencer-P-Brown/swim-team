from flask import Blueprint, render_template
from ..views import users


def generate_users_blueprint(config):
    blueprint = Blueprint('users', __name__)
    # blueprint.add_url_rule('/users', methods=['GET'], view_func=users.get_users.as_view('GetUsers'))
    blueprint.add_url_rule('/users', methods=['GET'], view_func=users.get_users)
    return blueprint
