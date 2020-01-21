import urllib2
from flask import Flask
from flask.ext.testing import LiveServerTestCase 

# Testing with LiveServer
class MyTest(LiveServerTestCase):
  # if the create_app is not implemented NotImplementedError will be raised
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app 

    def test_flask_application_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200) 

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_first_test_page_status_code(self):
        response = self.client.get('/testAlg')
        self.assertEquals(response.status_code, 200)

    def test_extended_input_page_status_code(self):
        response = self.client.get('/test/data%20is%20fun')
        self.assertEquals(response.status_code, 200)

    def test_extended_input_page_status_code_2(self):
        response = self.client.get('/test/data is fun')
        self.assertEquals(response.status_code, 200)

    def test_input_page_status_code(self):
        response = self.client.get('/test/data')
        self.assertEquals(response.status_code, 200)

    def test_alg_page_status_code(self):
        response = self.client.get('/alg/testInput')
        self.assertEquals(response.status_code, 200)


        

    

    