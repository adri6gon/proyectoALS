import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from model.book import Book


class deleteBook(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            access_link = users.create_logout_url("/")
            id = int(self.request.get("id"))
            book = Book.get_by_id(id)

            template_values = {
                    "book": book,
                    "titleView": "Tabla de borrado",
                    "user": user.email(),
                    "access_link": access_link
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("deleteBook.html", **template_values))

    def post(self):
        id = int(self.request.get("idem"))
        bookDelete = Book.get_by_id(id)
        bookDelete.key.delete()
        self.redirect("/seeBooks")

app = webapp2.WSGIApplication([
    ('/deleteBook', deleteBook),
], debug=True)