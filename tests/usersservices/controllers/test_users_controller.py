import json

from tornado.escape import json_encode
from tornado.testing import AsyncHTTPTestCase, gen_test

from unittest.mock import patch

from usersservices.controllers.users_controller import UsersController
from usersservices.server import make_app

class TestUsersController(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    def test_create_invalid_user(self):
        body = json_encode({})
        response = self.fetch('/api/users', method='POST', body=body)
        data = json.loads(response.body.decode())["data"]
        self.assertEqual(response.code, 422)
        self.assertEqual(len(data["errors"]), 3)

    def test_create_valid_user(self):
        with patch('usersservices.controllers.users_controller.create_user') as c:
            c.return_value = "uidhash"

            body = json_encode(self.get_valid_user())
            response = self.fetch('/api/users', method='POST', body=body)
            data = json.loads(response.body.decode())["data"]

        self.assertEqual(response.code, 201)
        self.assertFalse("errors" in data)

    def get_valid_user(self):
        return {
            "uid": "",
            "name": "a name",
            "email": "an_email@example.com",
            "password": "123456"
        }
