from app import app
import unittest
import os 



class WebTestCase(unittest.TestCase):
    
    def test_database (self): 
        tester = os.path.exists ("flaskr.db") 
        self.assertTrue(tester)


    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_other(self):
        tester = app.test_client(self)
        response = tester.get('test', content_type='html/text')
        self.assertEqual(response.status_code, 404)
    



if __name__ == '__main__':
    unittest.main()