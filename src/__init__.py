from flask import Flask

from src.cache import cache
from src.myweb import myweb_bp
import requests


def create_app():
    """Creates the app with cache instance and Blueprints registered"""
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(myweb_bp)