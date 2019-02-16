
from tests.v1.base_test import BaseTest
import unittest
import json


class TestOffices(BaseTest):
    def test_create_party(self):

        resp = self.client.post(path='/api/v1/parties', data=self.create_party, content_type='application/json')
        self.assertEqual(resp.status_code, 201)



    def test_get_all_parties(self):
        self.client.post(path='/api/v1/parties', data=self.create_party, content_type='application/json')
        res = self.client.get(path='/api/v1/parties', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_party(self):
        self.client.post(path='/api/v1/parties', data=self.create_party, content_type='application/json')
        res = self.client.get(path='/api/v1/parties/1')
        self.assertEqual(res.status_code, 200)

    def test_update_party(self):
        self.client.post(path='/api/v1/parties', data=self.create_party, content_type='application/json')
        res = self.client.patch(path='/api/v1/parties/2')
        self.assertEqual(res.status_code, 200)

    def test_delete_party(self):
        self.client.post(path='/api/v1/parties', data=self.create_party, content_type='application/json')
        res = self.client.delete(path='/api/v1/parties/2')
        self.assertEqual(res.status_code, 404)
    def test_get_party_index(self):
        self.client.post(path='/api/v1/index', data=self.create_party, content_type='application/json')
        res = self.client.get(path='/api/v1/index')
        self.assertEqual(res.status_code, 200)

        print(self.client.post)


# import unittest
# import json
# from tests.v1 import base_test
#
# def test_getting_all_parties(self):
#     ## test endpoint for getting all parties
#     response=self.client.get(path='api/v1/parties')
#     self.assertEqual(response.status_code,200)
#
# def test_getting_single_party(self):
#      path = '/api/v1/parties'
#      res=self.client.get(path='api/v1/parties<partyID>')
#      self.assertEquals(res.status_code,200)
#
# def test_editing_a_single_party(self):
#     post = self.client.post(path='api/v1/parties', data=json.dumps(self.data), content_type='application/json')
#     partyID = post.json["data"][0]['partyID']
#     path = '/api/v1/parties{}'.format(partyID)
#     response = self.client.put(path, data=json.dumps(self.update), content_type='application/json')
#     self.assertEqual(response.status_code, 404)
#
# def test_deleting_a_party(self):
#     post = self.client.post(path='api/v1/parties', data=json.dumps(self.data),
#                             content_type='application/json')
#     id = post.json["data"][0]['partyID']
#     path = '/api/v1/parties/{}'.format(id)
#     response = self.client.delete(path, content_type='application/json')
#     self.assertEqual(response.status_code, 200)
#
# def test_posting_a_party(self):
#     resp = self.post()
#     self.assertEqual(resp.status_code, 200)
#     self.assertTrue(resp.json["data"][0]['partyID'])
#     self.assertEqual(resp.json['status'], 200)
#
#
#
def tearDown(self):
    self.app=None



if __name__ == '__main__':
    unittest.main


