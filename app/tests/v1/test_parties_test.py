from .base_test import BaseTest
from app import create_app
import unittest, json
app = create_app()
testapp = app.test_client()

 class TestParty(BaseTest):

    def test_create_party(self):
            response = self.post(self.party1)

    def test_create_party_all_null(self):
            response = self.post({})
            self.assertEqual(response.status_code, 400)
        

    def post(self, data):
            return self.client.post(path="api/v1/parties", data=json.dumps(data), content_type='application/json')
    
    def test_get_all_political_parties(self):
            response=self.client.get(path='api/v1/parties')
            self.assertEqual(response.status_code,200)


    def test_get_by_id(self):
            response=self.client.get(path='api/v1/parties')
            self.assertEqual(response.status_code,200)