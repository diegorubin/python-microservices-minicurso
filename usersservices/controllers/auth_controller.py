from tornado_json.requesthandlers import APIHandler
from tornado_json import schema

from usersservices.services.auth import auth as auth_service

class AuthController(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "email": {"type": "string"},
                "password": {"type": "string"}
            }
        },
        input_example={
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
                        "password": {"type": "string"}
                    }
                }
            }
        },
        output_example={
            "message": "auth success",
            "user": {
                "email": "user.name@example.com"
            }
        },
    )
    def post(self):
        user = auth_service(self.body["email"], self.body["password"])
        if user is not None:
            return {
                "message": "auth success",
                "user": user.attributes
            }
        else:
            self.set_status(401)
            return {
                "message": "auth failed",
                "user": {
                    "email": self.body["email"]
                }
            }

