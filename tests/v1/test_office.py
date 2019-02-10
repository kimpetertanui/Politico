from tests.v1.base_test import BaseTest
import unittest
from app import app_config
import json

# testapp = app.test_client()

class TestOffices(BaseTest):
    def test_create_office(self):

        resp = self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
        self.assertEqual(resp.status_code, 201)



    def test_get_all_offices(self):
        self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
        res = self.client.get(path='/api/v1/offices', content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_office(self):
        self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
        res = self.client.get(path='/api/v1/offices/1')
        self.assertEqual(res.status_code, 200)

    # def test_update_office(self):
    #     self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
    #     res = self.client.patch(path='/api/v1/offices/3')
    #     self.assertEqual(res.status_code, 200)

    def test_delete_office(self):
        self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
        res = self.client.delete(path='/api/v1/offices/2')
        self.assertEqual(res.status_code, 200)
        print(res)

    # def get_missing_office(self):
    #     self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
    #     res = self.client.get(path='/api/v1/offices/kfjfhfhdfh')
    #     self.assertEqual(res.status_code, 400)

    #
    # def test_get_missing_office(self):
    #     res = self.get_missing_office()
    #     self.assertEqual(res.status_code, 400)
    #     return res


    # def test_getting_all_offices(self):
    #     ## test endpoint for getting all offices
    #     response=self.client.get(path='api/v1/offices')
    #     self.assertEqual(response.status_code,200)
    #
    # def test_getting_single_office(self):
    #      path = '/api/v1/offices'
    #
    #      res=self.client.get(path='api/v1/offices')
    #      self.assertEquals(res.status_code,200)
    #
    # def test_editing_a_single_office(self):
    #     post = self.client.post(path='api/v1/offices', data=json.dumps(self.office_data), content_type='application/json')
    #     id= post.json["data"][0]['id']
    #     path = '/api/v1/parties{}'.format(id)
    #     response = self.client.put(path, data=json.dumps(self.office_update), content_type='application/json')
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_deleting_an_office(self):
    #     post = self.client.post(path='api/v1/offices', data=json.dumps(self.office_data), content_type='application/json')
    #     id = post.json["data"][0]['id']
    #     path = '/api/v1/offices/{}'.format(id)
    #     response = self.client.delete(path, content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_posting_an_office(self):
    #     res = self.post()
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(res.json["data"][0]['id'])
    #     self.assertEqual(res.json['status'], 200)


if __name__ == '__main__':
        unittest.main


