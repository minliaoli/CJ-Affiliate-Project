from django.test import TestCase
from .pyrebase_settings import db

# Create your tests here.
class databaseTest(SimpleTestCase)

    def test_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
    
    def test_db_status(self):
        response = db.child("products").get()
        self.assertTrue(response)

    