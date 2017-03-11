import tornado.web

class UsersController(tornado.web.RequestHandler):

    def get(self):
        self.success({'users': []})

