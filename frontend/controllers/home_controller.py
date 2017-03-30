from frontend.controllers.base_controller import BaseController

class HomeController(BaseController):
    def get(self):
        self.render("home.html", user=self.get_current_user())

