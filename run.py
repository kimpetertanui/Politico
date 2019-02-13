from app import  create_app
from flask import Flask
from app.api.v1.views.views_office import v1
from app.api.v1.views.views_party import b_party
app = create_app('development')
# app = Flask(__name__)

app.register_blueprint(v1)
app.register_blueprint(b_party)


if __name__ == '__main__':
    app.run()