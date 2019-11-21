from unittest import TestCase
import json

from app import create_app
from db import db

app = create_app('TEST')


class TestSchool(TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()

    def test_post(self):
        obj_json = json.dumps({"name": "school_1"})
        response = app.test_client().post("/school", data=obj_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, [{"id": 1, "name": "school_1"}])
