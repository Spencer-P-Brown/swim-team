import json

from flask import request, jsonify

from swimteam_server.extensions import DB


# @app.route('/get-users', methods=['POST', 'GET'])
def get_users():
    users = DB.query.all()
    return jsonify(users)
