from microservicesutils.resources import BaseResource

class User(BaseResource):

    def __init__(self, defaults = {}):
        self.init_attributes(['uid', 'name', 'email', 'password', 'image'],
            validations = {
                'name': {'required': True},
                'email': {'required': True},
                'password': {'required': True}
            },
            defaults = defaults
        )

