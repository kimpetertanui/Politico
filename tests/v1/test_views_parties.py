from run import app
import unittest
import json

from . import PoliticoTest




# class TestParties(PoliticoTest):
#     def test_post(self):
#          response = self.client.post("api/v1/parties", data=json.dumps({
#                 "party_name": "elihu",
#                 "hqAddress": "str",
#                  "logoUrl":"mim"
#             }), content_type="application/json")
#          result = json.loads(response.decode("utf-8"))
#          self.assertEqual(result['status'], 201)
    # def test_wrong_post(self):
    #     res = self.client.post("api/v1/addparty", data=json.dumps({
    #             "name": "567890",
    #             "slogan": "3456"
    #         }), content_type="application/json")
    #     result = json.loads(res.data.decode('utf-8'))
    #     self.assertEqual(result['status'], 400)

    # def test_get_party(self):
    #     res=self.client.get("api/v1/parties")
    #     result = json.loads(res.data.decode('utf-8'))
    #     self.assertEqual(result['status'], 200)
    # def test_empty_list(self):
    #     res=self.client.get("api/v1/parties")
    #     result=json.loads(res.data.decode('utf-8'))
    #     self.assertEqual(result['data'], [])
















class Test_parties(unittest.TestCase):
    def setUp(self):
        self.app=app
        self.client=self.app.test_client()
        self.data={
            "party_name":"TNA",
            "hqAddress":"Nairobi",
            "logoUrl":"Logo"
        }
        self.update={
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
        partyID = post.json['partyID']
        path = '/api/v1/parties{}'.format(partyID)
        response = self.client.put(path, data=json.dumps(self.update), content_type='application/json')
        self.assertEqual(response.status_code, 200)



    def tearDown(self):
        self.app=None



    if __name__ == '__main__':
        unittest.main


