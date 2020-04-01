"""Application routes"""
import requests
from flask import render_template

from src.cache import cache
from src.github import github_utils
from src.codewars import codewars_utils
from . import myweb_bp


@myweb_bp.route('/')
@cache.cached(timeout=20)  # cache this view for 20 seconds
def main_view():
    """Displays github repos"""
    try:
        return render_template('index.html', errors=False)
    except requests.exceptions.RequestException:
        return render_template('index.html', errors=True)



@myweb_bp.route('/')
@cache.cached(timeout=20)  # cache this view for 20 seconds
def github_view():
    """Displays github repos"""
    try:
        repos_list = github_utils.get_repos()
        return render_template('github.html', repos=repos_list, errors=False)
    except requests.exceptions.RequestException:
        return render_template('github.html', errors=True)



@myweb_bp.route('/codewars/')
@cache.cached(timeout=20)  # cache this view for 20 seconds
def codewars_view():
    """Displays codewars stats"""
    try:
        codewars_stats = codewars_utils.get_codewars_info()
        return render_template('index.html', skills=codewars_stats, errors=False)
    except requests.exceptions.RequestException:
        return render_template('codewars.html', errors=True)


