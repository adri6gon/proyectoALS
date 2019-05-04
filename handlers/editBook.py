import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

from model.book import Book
import model.book as book_mgt

class editBook(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            id = int(self.request.get("id"))

            book = Book.get_by_id(id)
            listTitle = {"isbn", "author", "avaliable", "type"}

            template_values = {
                "book": book,
                "listTitle": listTitle,
                "titleView": "Editar libro",
                "user": user.email(),
                "access_link": access_link
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("edit_book.html", **template_values))


    def post(self):
        id = int(self.request.get("id"))
        bookEdit = Book.get_by_id(id)
        if bookEdit:
            bookEdit.isbn = int(self.request.get("isbn"))
            bookEdit.type = self.request.get("type")
            bookEdit.title = self.request.get("title")
            bookEdit.author = self.request.get("author")
            bookEdit.avaliable = int(self.request.get("avaliable"))

            book_mgt.update(bookEdit)

        self.redirect("/seeBooks")

app = webapp2.WSGIApplication([
    ('/editBook', editBook),
], debug=True)