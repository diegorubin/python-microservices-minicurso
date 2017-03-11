from peewee import SqliteDatabase, Model

from microservicesutils.settings import *

database = SqliteDatabase(locals()["%s_DATABASE_PATH"%(CURRENT_APP)])
class BaseModel(Model):
    class Meta:
        database = database

def create_tables(tables):
    database.connect()
    database.create_tables(tables)

