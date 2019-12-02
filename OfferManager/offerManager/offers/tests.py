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

    def test_page_add(self):
        response = self.client.post('/api/offer')
        self.assertEquals(response.status_code, 201)

    def test_page_retreive(self):
        response = self.client.get('/api/offer')
        self.assertEquals(response.status_code, 201)

    def test_page_product_add(self):
       response = self.client.post('/api/product')
       self.assertEquals(response.status_code, 201)

    def test_page_product_retrieve(self):
       response = self.client.get('/api/product')
       self.assertEquals(response.status_code, 201)

    