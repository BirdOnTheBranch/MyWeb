from flask import Flask, request, g, redirect, url_for, render_template, flash, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import requests


# configuration
app = Flask(__name__)
app.config["SECRET_KEY"] = "rajsiosorqwnejrq39834tergm4"
app.config['DATABASE'] = 'flaskr.db'
app.config['DEBUG'] = True


# connect to database
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


# create the database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# open database connection
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# close database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



@app.route('/')
def index():
    """ Render apis github and codewars with user information in template """    
    
    #GitHub api information
    url_github = 'https://api.github.com/users/BirdOnTheBranch/repos'
    response = requests.get(url_github)
    if response.status_code == 200:
        github_json = response.json()
        my_repos = []
        for info in github_json:
            repos = {'name':info['name'], 'description': info['description'], 'url' : info['html_url']}
            my_repos.append(repos)


    #Codewars api information
    url_codewars = 'https://www.codewars.com/api/v1/users/BirdOnTheBranch'
    response = requests.get(url_codewars)
    if response.status_code == 200:
        codewars_json = response.json()
        skills = {   
            'name' : codewars_json['username'], 
            'honor' : codewars_json['honor'], 
            'completeChallenges' : codewars_json['codeChallenges']['totalCompleted']}

        my_skills = []
        my_skills.append(skills)


    
    return render_template("index.html", repos=my_repos, skills=my_skills)
   
    


if __name__ == '__main__':
    app.run(debug=True, port=8000)


