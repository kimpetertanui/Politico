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
        res = self.client.get(path='/api/v1/offices/3')
        self.assertEqual(res.status_code, 200)

    # def test_update_office(self):
    #     self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
    #     res = self.client.patch(path='/api/v1/offices/3')
    #     self.assertEqual(res.status_code, 200)

    def test_delete_office(self):
        self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
        res = self.client.delete(path='/api/v1/offices/1')
        self.assertEqual(res.status_code, 200)
        print(res)

    def get_missing_office(self):
        self.client.post(path='/api/v1/offices', data=self.create_office, content_type='application/json')
        res = self.client.get(path='/api/v1/offices/1')
        self.assertEqual(res.status_code, 400)
    #
    # def test_get_office_home(self):
    #     self.client.post(path='/api/v1/home', data=self.create_party, content_type='application/json')
    #     res = self.client.get(path='/api/v1/home')
    #     self.assertEqual(res.status_code, 200)


    #
    # def test_get_missing_office(self):
    #     res = self.get_missing_office()
    #     self.assertEqual(res.status_code, 400)
    #     return res





if __name__ == '__main__':
        unittest.main


