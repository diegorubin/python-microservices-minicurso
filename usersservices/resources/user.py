from microservicesutils.resources import BaseResource

class User(BaseResource):

    def __init__(self, defaults = {}):
        self.init_attributes(['name', 'email', 'password'], {
            'validations': {
                'name': {'required': True},
                'email': {'required': True},
                'password': {'required': True}
            },
            'defaults': defaults
        })

