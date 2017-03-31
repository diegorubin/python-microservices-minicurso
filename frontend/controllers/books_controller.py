from tornado_json.requesthandlers import APIHandler

from frontend.services.book import index, get
from frontend.services.comment import get as get_comments

from frontend.controllers.base_controller import BaseController

class BooksController(BaseController):
    def get(self):
        self.render("books.html", books = index())

class BookController(BaseController):
    def get(self, isbn):
        self.render(
            "book.html",
            book = get(isbn),
            comments = get_comments('book', isbn),
            user = self.get_current_user()
        )

