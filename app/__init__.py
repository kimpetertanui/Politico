from flask import Flask, jsonify, make_response, request

from app.api.v1.views.views_office import v1
from app.api.v1.views.views_party import b_party

def create_app(config_name='development'):
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(b_party)
    return app