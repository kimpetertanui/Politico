from run import app
import unittest
import json


class Test_Offices(unittest.TestCase):
    def setUp(self):
        self.app=app
        self.client=self.app.test_client()
        self.office_data={
            "id": 1,
            "name":"my",
            "type":"legislattive",

        }
        self.office_update={
            "id": 1,
            "name":"my",
            "type":"legislattive",
        }

    def post(self, path='/api/v1/offices', office_data={}):
        if not office_data:
            office_data = self.office_data

        resp = self.client.post(path='/api/v1/parties', data=json.dumps(self.office_data), content_type='application/json')
        return resp

    def test_getting_all_offices(self):
        ## test endpoint for getting all offices
        response=self.client.get(path='api/v1/offices')
        self.assertEqual(response.status_code,200)

    def test_getting_single_office(self):
         path = '/api/v1/offices'

         res=self.client.get(path='api/v1/offices')
         self.assertEquals(res.status_code,200)

    def test_editing_a_single_office(self):
        post = self.client.post(path='api/v1/offices', data=json.dumps(self.office_data), content_type='application/json')
        id= post.json["data"][0]['id']
        path = '/api/v1/parties{}'.format(id)
        response = self.client.put(path, data=json.dumps(self.office_update), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_deleting_an_office(self):
        post = self.client.post(path='api/v1/offices', data=json.dumps(self.office_data), content_type='application/json')
        id = post.json["data"][0]['id']
        path = '/api/v1/offices/{}'.format(id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def tearDown(self):
        self.app=None



    if __name__ == '__main__':
        unittest.main


