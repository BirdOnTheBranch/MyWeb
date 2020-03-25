from app import app, create_app
from nose.tools import assert_true, assert_is_none, assert_list_equal
from mock import Mock, patch
from app import github_display
import responses
import requests
import unittest 
import os 


class WebTestCase(unittest.TestCase):
    """Test app web-personal."""


    def test_index(self):
        """Index path render template."""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_other(self):
        """ Incorrect path returns 404 """
        tester = app.test_client(self)
        response = tester.get('test', content_type='html/text')
        self.assertEqual(response.status_code, 404)


    def test_request_response(self):
        """Valid json dict api codewars in template"""
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn('Codewars records', response.data)


    def test_database (self): 
        """Create data base."""
        tester = os.path.exists ("flaskr.db") 
        self.assertTrue(tester)


class MainTestCase(unittest.TestCase):
    """Class with basic tests."""

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
        'leaderboardPosition': 420,
        'codeChallenges': {
            'totalAuthored': 1,
            'totalCompleted': 77,
        },
        'ranks': {
            'overall': {
                'name': '3 kyu',
            },
            'languages': {
                'python': {
                    'name': '4 kyu',
                    'score': 9000,
                }
            }
        }
    }


    def setUp(self):
        """Set up test environment."""
        super(MainTestCase, self).setUp()
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
        self.assertIn(b'9000', response.data)



if __name__ == '__main__':
    unittest.main()
    