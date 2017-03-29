from peewee import CharField

from microservicesutils.database import BaseModel

class UserModel(BaseModel):
    name = CharField()
    email = CharField()
    password = CharField()

def users_as_resource(models):
    return [user_as_resource(model).attributes for model in models]

def user_as_resource(model):
    resource = User()
    for attribute in resource.attributes:
        resource.set_attribute(attribute, getattr(model, attribute))

    return resource

def create_user(attributes):
    print('\n\n\n\n\n\n')
    print(attributes)
    print('\n\n\n\n\n\n')
    user = UserModel.create(
        name=attributes['name'],
        email=attributes['email'],
        password=attributes['password']
    )
    return user
