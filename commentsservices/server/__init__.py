import tornado
import tornado.web
import os

from microservicesutils import logger
from microservicesutils.database import create_tables
from microservicesutils.logger import general
from microservicesutils.settings import COMMENTS_SERVER_PORT, DEBUG

from commentsservices.models.comment import CommentModel

from commentsservices.controllers.comments_controller import ListCommentsController
from commentsservices.controllers.comments_controller import CommentsController

def make_app():
    app = tornado.web.Application(
        [
            (r"/api/comments", CommentsController),
            (r"/api/comments/(\w+)/(\w+)", ListCommentsController),
        ],
        debug=DEBUG
    )
    return app


def start():

    create_tables([CommentModel])

    logger.initialize_logging('comments')

    app = make_app()
    app.listen(COMMENTS_SERVER_PORT)

    general.info("starting server")

    tornado.ioloop.IOLoop.current().start()
