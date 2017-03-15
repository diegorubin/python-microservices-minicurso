from tornado_json.requesthandlers import APIHandler

from usersservices.models.user import UserModel
from usersservices.resources.user import users_as_resource

class UsersController(APIHandler):

    def get(self):
        users = UserModel.select()
        self.success({'users': users_as_resource(users)})

