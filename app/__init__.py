from flask import Flask
from instance.config import app_config
from app.v1.views.parties import api

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    #app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(api)
    return app