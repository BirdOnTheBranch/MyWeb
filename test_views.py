from app import app, github_display
from nose.tools import assert_true, assert_is_none, assert_list_equal

import responses
import requests
import unittest 
import os 


def create_app():
    """Creates the app """
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'

    return app


class WebTestCase(unittest.TestCase):
    """Test simple app web-personal."""


    def test_index(self):
        """Index path render html template."""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_other(self):
        """ Incorrect path returns 404 """
        tester = app.test_client(self)
        response = tester.get('test', content_type='html/text')
        self.assertEqual(response.status_code, 404)


class ApisTestCase(unittest.TestCase):
    """testing apis mock json and response."""

    mock_repos = [
        {
            'name': 'repo1',
            'html_url': 'https://github.com/username/repo1',
            'description': 'First repo of user',
        },
        {
            'name': 'repo2',
            'html_url': 'https://github.com/username/repo2',
            'description': 'Last repo of user',
        }
    ]

    mock_codewars_stats = {
        'username': 'Adrian Lamo',
        'honor': 420,
        'codeChallenges': {
            'totalCompleted': 77,
        },
        'ranks': {
            'overall': {
                'name': '3 kyu',
            },
            'languages': {
                'python': {
                }
            }
        }
    }


    def setUp(self):
        """Set up test environment."""
        super(ApisTestCase, self).setUp()
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app
        self.test_client = app.test_client()
        self.assertEqual(app.debug, False)

        responses.add(responses.GET, 'https://api.github.com/users/BirdOnTheBranch/repos',
                      json=self.mock_repos,
                      status=200)
        responses.add(responses.GET, 'https://www.codewars.com/api/v1/users/BirdOnTheBranch',
                      json=self.mock_codewars_stats,
                      status=200)


    @responses.activate
    def test_html_contains_personal_information(self):
        """Test template is rendered with 'personal information' string."""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Adrian Lamo', response.data)



if __name__ == '__main__':
    unittest.main()
    