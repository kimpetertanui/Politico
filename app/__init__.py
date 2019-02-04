from flask import Flask, jsonify, make_response, request

from app.api.v1.views.views_office import v1

def create_app(config_name='development'):
    app = Flask(__name__)
    app.register_blueprint(v1)

    return app