import webapp2
from google.appengine.api import users
from webapp2_extras import jinja2

import model.book as book_mgt

class addBooks(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")

            template_values = {
                "titleView": "Anadir libro",
                "user": user.email(),
                "access_link": access_link
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("add_book.html", **template_values))

    def post(self):
        book = book_mgt.create_empty_book()
        book.isbn = int(self.request.get("isbn"))
        exists = book_mgt.retrieve(book)
        book.type = self.request.get("type")
        book.title = self.request.get("title")
        book.author = self.request.get("author")
        book.avaliable = int(self.request.get("avaliable"))

        if not exists:
            book_mgt.update(book)

        self.redirect("/seeBooks")

app = webapp2.WSGIApplication([
    ('/addBooks', addBooks),
], debug=True)