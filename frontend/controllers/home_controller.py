import tornado.web

class HomeController(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")
