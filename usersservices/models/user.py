from peewee import CharField

from hashlib import sha256, md5

from microservicesutils.database import BaseModel
from usersservices.resources.user import User

class UserModel(BaseModel):
    uid = CharField()
    name = CharField()
    email = CharField()
    password = CharField()

def users_as_resource(models):
    return [user_as_resource(model).attributes for model in models]

def user_as_resource(model):
    resource = User()
    for attribute in resource.attributes:
        if hasattr(model, attribute):
            resource.set_attribute(attribute, getattr(model, attribute))
    email = resource.get_attribute('email').encode('utf-8')
    resource.set_attribute('image', md5(email).hexdigest())
    return resource

def list_users():
    return UserModel.select()

def find_user_by_uid(uid):
    return UserModel.select().where(UserModel.uid == uid).first()

def create_user(attributes):
    password_hash = sha256()
    password_hash.update(attributes['password'].encode('utf-8'))

    uid_hash = sha256()
    uid_hash.update(attributes['email'].encode('utf-8'))

    user = UserModel.create(
        uid= uid_hash.hexdigest(),
        name=attributes['name'],
        email=attributes['email'],
        password=password_hash.hexdigest()
    )
    return user.uid

def find_user_by_email_and_password(email, password):
    password_hash = sha256()
    password_hash.update(password.encode('utf-8'))
    users = (
        UserModel.select()
        .where(UserModel.email == email, UserModel.password == str(password_hash.hexdigest()))
    )
    return user_as_resource(users.first()) if len(users) > 0 else None

