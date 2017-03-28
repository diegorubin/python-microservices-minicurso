import tornado
import tornado.web
import os

from microservicesutils import logger
from microservicesutils.logger import general
from microservicesutils.settings import FRONTEND_SERVER_PORT, DEBUG

from frontend.controllers.auth_controller import AuthController
from frontend.controllers.home_controller import HomeController

class Static(tornado.web.RequestHandler):

    def get(self, static_file):
        self.render("static/%s" % static_file)

def make_app():
    app = tornado.web.Application(
        [
            (r"/", HomeController),
            (r"/auth", AuthController),
            (r"/static/([\w_\.-]+)", Static),
        ],
        template_path=os.path.join(os.path.dirname(__file__), '..', 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), '..', 'static'),
        debug=DEBUG
    )
    return app


def start():

    logger.initialize_logging('frontend')

    app = make_app()
    app.listen(FRONTEND_SERVER_PORT)

    general.info("starting server")

    tornado.ioloop.IOLoop.current().start()
