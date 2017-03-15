import tornado
import tornado.web
import os

from microservicesutils import logger
from microservicesutils.database import create_tables
from microservicesutils.logger import general
from microservicesutils.settings import USERS_SERVER_PORT, DEBUG

from usersservices.models.user import UserModel

from usersservices.controllers.users_controller import UsersController

def make_app():
    app = tornado.web.Application(
        [
            (r"/api/users", UsersController),
        ],
        debug=DEBUG
    )
    return app


def start():

    create_tables([UserModel])

    logger.initialize_logging('users')

    app = make_app()
    app.listen(USERS_SERVER_PORT)

    general.info("starting server")

    tornado.ioloop.IOLoop.current().start()
