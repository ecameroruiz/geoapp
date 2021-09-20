"""
Initialize Flask App
"""

from flask import Flask
from config import app_config
from routes.geoapp import geoapp_bp
from routes.registration import registration_bp


def create_app(config):
    """
    Initialize Flask App

    :param str config: Environment Config
    :return: Created Flask App
    """
    # create flask app
    app = Flask(__name__)

    # get config name
    config_name = app_config[config]

    # set configuration
    app.config.from_object(config_name)

    # register blueprints
    app.register_blueprint(geoapp_bp)
    app.register_blueprint(registration_bp)

    return app
