from tornado_json.requesthandlers import APIHandler

from frontend.services.auth import is_valid_user

class AuthController(APIHandler):
    def post(self):
        if is_valid_user(self.get_body_argument('email'), self.get_body_argument('password')):
            self.success({})
        else:
            self.set_status(401)
            self.fail({'message': 'Login falhou! Verifique email e senha.'})

