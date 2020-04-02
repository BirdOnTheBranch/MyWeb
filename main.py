from flask import Flask, render_template
import requests


app = Flask(__name__)
app.config['DEBUG'] = True

def create_app():
    """Creates the app """
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'

    return app


@app.route('/')
def github_display():
    """Render api github with user information in template """    
    
    #GitHub api information
    url_github = 'https://api.github.com/users/BirdOnTheBranch/repos'
    response = requests.get(url_github)
    if response.status_code == 200:
        github_json = response.json()
        my_repos = []
        for info in github_json:
            repos = {'name':info['name'], 'description': info['description'], 'url' : info['html_url']}
            my_repos.append(repos)


    # Codewars api information
    url_codewars = 'https://www.codewars.com/api/v1/users/BirdOnTheBranch'
    response = requests.get(url_codewars)
    if response.status_code == 200:
        stats = response.json()
        skills = {   
            'username': stats['username'],
            'honor' : stats['honor'], 
            'overall_rankname': stats['ranks']['overall']['name'],
            'challenges_completed': stats['codeChallenges']['totalCompleted'],
            'languages': stats['ranks']['languages']}

    return render_template("index.html", repos=my_repos, skills=skills)



if __name__ == '__main__':
    app.run(debug=True, port= 8000, host='0.0.0.0')


