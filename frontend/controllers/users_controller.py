from tornado_json.requesthandlers import APIHandler

from frontend.services.user import create, index
from frontend.controllers.base_controller import BaseController

class UsersController(BaseController):
    def get(self):
        self.render("users.html", users = index())

class UsersAPIController(APIHandler):

    def post(self):
        user = {
            "name": self.get_body_argument('name'),
            "email": self.get_body_argument('email'),
            "password": self.get_body_argument('password')
        }
        try:
            create(user)
            self.set_secure_cookie("user", self.get_body_argument('email'))
            self.success({'message': 'Usuário criado com sucesso!'})
        except:
            self.set_status(422)
            self.fail({'message': 'Não foi possível criar o usuário'})

