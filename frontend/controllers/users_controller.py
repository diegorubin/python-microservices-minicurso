from tornado_json.requesthandlers import APIHandler

from microservicesutils.logger import application

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
            result = create(user)
            self.set_secure_cookie("user", result['uid'])
            self.success({'message': 'Usuário criado com sucesso!'})
        except Exception as e:
            application.error('error on create user in api: ' + str(e))
            self.set_status(422)
            self.fail({'message': 'Não foi possível criar o usuário'})

