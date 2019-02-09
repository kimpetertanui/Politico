
import unittest
import json
from tests.v1 import parties_base_test

def test_getting_all_parties(self):
    ## test endpoint for getting all parties
    response=self.client.get(path='api/v1/parties')
    self.assertEqual(response.status_code,200)

def test_getting_single_party(self):
     path = '/api/v1/parties'
     res=self.client.get(path='api/v1/parties<partyID>')
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
    resp = self.post()
    self.assertEqual(resp.status_code, 200)
    self.assertTrue(resp.json["data"][0]['partyID'])
    self.assertEqual(resp.json['status'], 200)



def tearDown(self):
    self.app=None



if __name__ == '__main__':
    unittest.main


