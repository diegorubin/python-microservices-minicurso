from peewee import CharField

from microservicesutils.database import BaseModel

class UserModel(BaseModel):
    name = CharField()
    email = CharField()
    password = CharField()

