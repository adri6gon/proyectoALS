import webapp2
from google.appengine.api import users
import model.book as book_mgt
import model.reserve as reserve_mgt


class returnBook(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        isbn = int(self.request.get("isbn"))
        reservesUser = reserve_mgt.getReserves(user.email())
        book = book_mgt.getBook(isbn)
        if user and reserve_mgt.retrieve(isbn):

            for res in reservesUser:
                if res.isbn == isbn:
                    res.key.delete()

            number = book.avaliable + 1
            book.avaliable = number

            book_mgt.update(book)

        self.redirect("/myReserves")


app = webapp2.WSGIApplication([
    ('/returnBook', returnBook),
], debug=True)