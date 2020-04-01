"""Main module of the application"""

from flask import Blueprint

myweb_bp = Blueprint('myweb', __name__, template_folder='templates')

from . import routes