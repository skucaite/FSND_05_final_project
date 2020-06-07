import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Guide, Travel, db, db_drop_and_create_all

user_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkOGRhMjMzMzIwMDMwYjdmNWRmNTRiIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTUwNzM1MCwiZXhwIjoxNTkxNTE0NTUwLCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDpndWlkZXMiLCJyZWFkOnRyYXZlbHMiXX0.GuKAZX5gd0GrxhFHjdaVq4uaoenWmwZUqN_wAnm-ECqJg-kB0lgz0DR_oa1FXAYbWsFNs3F-rXbR3eQCekJtzBC76K6A_c4LRSS1mZ2sixxc7aLwXB2Ai0WgjNuCm2D2YQX7UlGoAv1fRqRLDSKbc9TtPwy6Cv9bLVxdE0IpU5tF-PWhccx3Opw_hY3E63m2carUJnVzK8v4LxZfTVXYpGRpJnaFLX-iEK3Bo4q4Vy1CntHloM8GmGb6gcxZwt8d3cA6jh7v91gFHCfpR35l3hRcAqIrUHUBC1YRqRJV8f9UA-4dDLgQnKkyK8Gs62pdRFyzA_gYOsYAH9J4ianh1A'

admin_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InZkQUlSM0h3aFBMZTFkZTc1dEJJQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcnp3ODA1Yi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkYjZhOGNhMTFjN2YwMDFhMTZjZTYzIiwiYXVkIjoidHJhdmVsYm9vayIsImlhdCI6MTU5MTUwNzU1NCwiZXhwIjoxNTkxNTE0NzU0LCJhenAiOiJSU2lsV0dDNUpOclp0Z1BzTTlDTEs2WDVOWk1ORld0SiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmd1aWRlcyIsImNyZWF0ZTp0cmF2ZWxzIiwiZGVsZXRlOmd1aWRlcyIsImRlbGV0ZTp0cmF2ZWxzIiwiZWRpdDpndWlkZXMiLCJlZGl0OnRyYXZlbHMiLCJyZWFkOmd1aWRlcyIsInJlYWQ6dHJhdmVscyJdfQ.gr_YwtLVPxJoHyfElteo0axRAELA1MBQAGPcWG5V5L83lq1bsjeLrvN5zwYtFlYaOIm2PfBZ3VHJ5v8J_H-B2AXzqEz4TYl4WAeXWepRAbvQHvXM8O4rJJJJHM_uHLvRDtrbv6rCNu0OKTnxBUpIgBuhuc14YkvaD5aInGVGEPjLTSF_KIaTVTlhw4W5z88609owlkbtCYAnJZjm6-KD8rB7v76StRu16Vyb7aBVCNYv5vrBQWjzBaI4JQ35L3GWZ59v7vQl2yRbBqdFIP3gmfXc14_gFuvdKntB1rVUne6w8fg8obNdE6zYy-y7rWdd75xqytQCP6Yf7Qmlt8s2pA'



class TriviaTestCase(unittest.TestCase):
    """This class represents the travelapi test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "travelapi_test"
        self.database_path = "postgresql://postgres@localhost:5432/travelapi_test"
        setup_db(self.app)

        self.new_guide = {
          'name': 'Tom',
          'surname': 'Johnson',
          'phone': '84579623'
        }

        self.new_travel = {
          'title': 'Visit Berlin',
          'content': 'See a lot of Berlin sightseeings',
          'guide_id': '1'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


#  Test for travels GET
#----------------------------------------------------------------------------#
    def test_get_travels(self):
        res = self.client().get('/travels', headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['travels'])

    def test_404_if_travels_not_found(self):
        res = self.client().get('/travels5', headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_401_if_travels_unauthorized(self):
        res = self.client().get('/travels')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


#  Test for guides GET
#----------------------------------------------------------------------------#
    def test_get_guides(self):
        res = self.client().get('/guides', headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['guides'])

    def test_404_if_guides_not_found(self):
        res = self.client().get('/guides5', headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_401_if_guides_unauthorized(self):
        res = self.client().get('/guides')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


#  Test for travels POST
#----------------------------------------------------------------------------#
    def test_create_new_travel(self):
        res = self.client().post('/travels', json=self.new_travel, headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['travels'])

    def test_404_if_travel_creation_not_allowed(self):
        res = self.client().post('/categories', json=self.new_travel, headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_403_if_travel_creation_forbidden(self):
        res = self.client().post('/travels', json=self.new_travel, headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


#  Test for guides POST
#----------------------------------------------------------------------------#
    def test_create_new_guide(self):
        res = self.client().post('/guides', json=self.new_guide, headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['guides'])

    def test_404_if_guide_creation_not_allowed(self):
        res = self.client().post('/categories', json=self.new_guide, headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_403_if_guide_creation_forbidden(self):
        res = self.client().post('/guides', json=self.new_guide, headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


#  Test for travels PATCH
#----------------------------------------------------------------------------#
    def test_edit_travel(self):
        insert_res = self.client().post('/travels', json=self.new_travel, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        travel_id = insert_data['created']

        res = self.client().patch(f'/travels/{travel_id}', json={'title': 'Visit New City'}, headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['travels'])

    def test_404_if_travel_does_not_exist(self):
        res = self.client().patch('/travels/5000', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_403_if_travel_edition_forbidden(self):
        insert_res = self.client().post('/travels', json=self.new_travel, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        travel_id = insert_data['created']

        res = self.client().patch(f'/travels/{travel_id}', json={'title': 'Visit New City'}, headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


#  Test for guides PATCH
#----------------------------------------------------------------------------#
    def test_edit_guide(self):
        insert_res = self.client().post('/guides', json=self.new_guide, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        guide_id = insert_data['created']

        res = self.client().patch(f'/guides/{guide_id}', json={'name': 'Petras'}, headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['guides'])

    def test_404_if_guide_does_not_exist(self):
        res = self.client().patch('/guides/5000', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_403_if_guide_edition_forbidden(self):
        insert_res = self.client().post('/guides', json=self.new_guide, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        guide_id = insert_data['created']

        res = self.client().patch(f'/guides/{guide_id}', json={'name': 'Petras'}, headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


#  Test for travels DELETE
#----------------------------------------------------------------------------#
    def test_delete_travel(self):
        insert_res = self.client().post('/travels', json=self.new_travel, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        travel_id = insert_data['created']

        res = self.client().delete(f'/travels/{travel_id}', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_404_if_travel_does_not_exist(self):
        res = self.client().patch('/travels/5000', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_403_if_travel_deletion_forbidden(self):
        insert_res = self.client().post('/travels', json=self.new_travel, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        travel_id = insert_data['created']

        res = self.client().delete(f'/travels/{travel_id}', headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


#  Test for guides DELETE
#----------------------------------------------------------------------------#
    def test_delete_guide(self):
        insert_res = self.client().post('/guides', json=self.new_guide, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        guide_id = insert_data['created']

        res = self.client().delete(f'/guides/{guide_id}', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_404_if_guide_does_not_exist(self):
        res = self.client().patch('/guides/5000', headers={"Authorization": "Bearer {}".format(admin_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_403_if_guide_deletion_forbidden(self):
        insert_res = self.client().post('/guides', json=self.new_guide, headers={"Authorization": "Bearer {}".format(admin_token)})
        insert_data = json.loads(insert_res.data)
        guide_id = insert_data['created']

        res = self.client().delete(f'/guides/{guide_id}', headers={"Authorization": "Bearer {}".format(user_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
