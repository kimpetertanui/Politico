import unittest
import json
from run import app

class Test_parties(unittest.TestCase):
    def setUp(self):
        self.app=app
        self.client=self.app.test_client()

    def test_get_parties(self):
        ## test endpoint for getting all parties
        response=self.client.get(path='api/v1/getAllParties')
        self.assertEqual(response.status_code,200)





    if __name__ == '__main__':
        unittest.main


