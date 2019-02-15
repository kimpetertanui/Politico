from flask import Flask, jsonify, make_response, request
from config import app_config
import psycopg2
import os
from app.api.v1.views.views_office import v1
from app.api.v2.views.views_user_signup import v2

from app.api.v1.views.views_party import b_party

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(v1)
    app.register_blueprint(b_party)
    app.register_blueprint(v2)
    return app