import json
import  unittest
from app import create_app

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app=create_app(config_name="testing")

        self.client= self.app.test_client()
        self.client1= self.app.test_client


        self.create_office=json.dumps({
            "id":1,
            "name":"Senator",
            "type":"Legislative"
        })

        self.create_party=json.dumps({

            "id":1,
             "party_name":"PNU",
              "hqAddress":"Nairobi",
               "logoUrl":"The Logo is Tuko Pamoja"

        })


    def tearDown(self):
        self.app.testing= False
    # def post(self, path='/api/v1/parties', data={}):
    #     if not data:
    #         data = self.data
    #
    #     resp = self.client.post(path='/api/v1/parties', data=json.dumps(self.data), content_type='application/json')
    #     return resp