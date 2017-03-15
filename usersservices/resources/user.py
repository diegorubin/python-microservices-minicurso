from microservicesutils.resources import BaseResource

class User(BaseResource):

    def __init__(self, options = {}):
        self.init_attributes(['name', 'email', 'password'])


def users_as_resource(models):
    return [user_as_resource(model) for model in models]

def user_as_resource(model):
    resource = User()
    for attribute in resource.attributes:
        resource.set_attribute(attribute, getattr(model, attribute))

    return resource

