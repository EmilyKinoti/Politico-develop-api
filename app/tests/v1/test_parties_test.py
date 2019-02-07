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

    def test_get_a_party(self,party_id):
        responec = sel.post({"id":1})
        self.assertEqual(responec.status_code, 200)

    def post(self, data):
        return self.client.post(path="api/v1/parties", data=json.dumps(data), content_type='application/json')
