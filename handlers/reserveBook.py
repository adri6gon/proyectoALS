import webapp2
from google.appengine.api import users
import model.book as book_mgt
from model.book import Book
import model.reserve as reserve_mgt


class reserveBook(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        id = int(self.request.get("id"))
        book = Book.get_by_id(id)

        if user and not reserve_mgt.retrieve(book.isbn):
            reserve = reserve_mgt.create_empty_reserve()
            reserve.email = users.get_current_user().email()

            number = book.avaliable - 1
            book.avaliable = number
            reserve.isbn = book.isbn

            book_mgt.update(book)
            reserve_mgt.update(reserve)

        self.redirect("/seeBooks")


app = webapp2.WSGIApplication([
    ('/reserveBook', reserveBook),
], debug=True)