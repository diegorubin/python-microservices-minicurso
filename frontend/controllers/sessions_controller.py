from tornado_json.requesthandlers import APIHandler

from frontend.services.auth import is_valid_user

class SessionsController(APIHandler):
    def post(self):
        user = is_valid_user(self.get_body_argument('email'), self.get_body_argument('password'))
        if not user is None:
            self.set_secure_cookie("user", user["uid"])
            self.success({'message': 'Login realizado com sucesso!'})
        else:
            self.set_status(401)
            self.fail({'message': 'Login falhou! Verifique email e senha.'})

    def delete(self):
        self.clear_cookie("user")
        self.success({'message': 'Logout realizado com sucesso!'})

