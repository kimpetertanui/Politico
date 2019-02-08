
import unittest
import json
from  run import  app
from . import PoliticoTest



class Test_parties(unittest.TestCase):
    def setUp(self):
        self.app=app
        self.client=self.app.test_client()
        self.data={
            "partyID": 1,
            "party_name":"TNA",
            "hqAddress":"Nairobi",
            "logoUrl":"Logo"
        }
        self.update={
            "partyID": 2,
            "party_name": "Jupilee",
            "hqAddress": "Eldoret",
            "logoUrl": "NewLogo"
        }

    def post(self, path='/api/v1/parties', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/api/v1/parties', data=json.dumps(self.data), content_type='application/json')
        return resp

    def test_getting_all_parties(self):
        ## test endpoint for getting all parties
        response=self.client.get(path='api/v1/parties')
        self.assertEqual(response.status_code,200)

    def test_getting_single_party(self):
         path = '/api/v1/parties'
         res=self.client.get(path='api/v1/parties')
         self.assertEquals(res.status_code,200)

    def test_editing_a_single_party(self):
        post = self.client.post(path='api/v1/parties', data=json.dumps(self.data), content_type='application/json')
        partyID = post.json["data"][0]['partyID']
        path = '/api/v1/parties{}'.format(partyID)
        response = self.client.put(path, data=json.dumps(self.update), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_deleting_a_party(self):
        post = self.client.post(path='api/v1/parties', data=json.dumps(self.data),
                                content_type='application/json')
        id = post.json["data"][0]['partyID']
        path = '/api/v1/parties/{}'.format(id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_posting_a_party(self):
        res = self.post()
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json["data"][0]['partyID'])
        self.assertEqual(res.json['status'],200)



    def tearDown(self):
        self.app=None



    if __name__ == '__main__':
        unittest.main


