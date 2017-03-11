from microservicesutils.resources import BaseResource

class User(BaseResource):

    def __init__(self, options = {}):
        self.init_attributes(['name', 'email', 'password'])

