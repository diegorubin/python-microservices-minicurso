import tornado.web

from frontend.services.user import get

class BaseController(tornado.web.RequestHandler):
    def get_current_user(self):
        uid = self.get_secure_cookie("user")
        if uid:
            user = get(uid.decode())
            return user

