from app import  create_app
from flask import Flask
from app.api.v1.views.views_office import v1
##app = create_app()
app = Flask(__name__)
app.register_blueprint(v1)
if __name__ == '__main__':
    app.run()