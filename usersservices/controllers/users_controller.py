from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

import json

from usersservices.resources.user import User
from usersservices.models.user import UserModel, create_user
from usersservices.models.user import users_as_resource, user_as_resource

class UsersController(APIHandler):

    def get(self):
        users = UserModel.select()
        self.success({'users': users_as_resource(users)})

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "name": {"type": "string"},
                "password": {"type": "string"}
            }
        },
        input_example={
            "name": "user name",
            "email": "user.name@example.com",
            "password": "a password",
        },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "user": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string"},
                        "name": {"type": "string"},
                        "password": {"type": "string"}
                    }
                }
            }
        },
        output_example={
            "message": "user created",
            "user": {
                "name": "user name",
                "email": "user.name@example.com",
                "password": "a password",
            }
        },
    )
    def post(self):
        user = User(self.body)
        if user.is_valid():
            create_user(user.attributes)
            self.set_status(201)
            return {
                'message': 'user created',
                'user': user.attributes
            }
        else:
            self.set_status(422)
            return {
                'message': 'wrong user',
                'user': user.attributes,
                'errors': user.errors
            }

