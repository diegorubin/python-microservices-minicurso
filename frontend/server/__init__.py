import tornado
import tornado.web
import os

from microservicesutils import logger
from microservicesutils.logger import general
from microservicesutils.settings import FRONTEND_SERVER_PORT, DEBUG

from frontend.controllers.comments_controller import CommentsAPIController
from frontend.controllers.home_controller import HomeController
from frontend.controllers.books_controller import BookController, BooksController
from frontend.controllers.sessions_controller import SessionsController
from frontend.controllers.users_controller import UsersController, UsersAPIController

class Static(tornado.web.RequestHandler):

    def get(self, static_file):
        self.render("static/%s" % static_file)

def make_app():
    app = tornado.web.Application(
        [
            (r"/", HomeController),
            (r"/sessions", SessionsController),
            (r"/users", UsersController),
            (r"/books", BooksController),
            (r"/books/(\w+)", BookController),
            (r"/api/users", UsersAPIController),
            (r"/api/comments", CommentsAPIController),
            (r"/static/([\w_\.-]+)", Static),
        ],
        template_path=os.path.join(os.path.dirname(__file__), '..', 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), '..', 'static'),
        debug=DEBUG,
        cookie_secret="c641ea2aaa462236d1963115e01e70b24277cf1814c503ca98fc0f70dd8bedfc"
    )
    return app


def start():

    logger.initialize_logging('frontend')

    app = make_app()
    app.listen(FRONTEND_SERVER_PORT)

    general.info("starting server")

    tornado.ioloop.IOLoop.current().start()
