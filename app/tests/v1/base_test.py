import unittest
from app import create_app

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        self.party1 = {
            "id":1,
            "name":"Party 1",
            "address": "Location 1",
            "logo":"photo/1"
        }
        self.party2 = {
            "id":1,
            "name":"Party 1",
            "hqAddress": "Location 1",
            "photoUrl":"photo/1"
        }

       

    def tearDown(self):
        self.app = None