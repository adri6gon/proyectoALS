import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from model.book import Book


class seeBooks(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:

            access_link = users.create_logout_url("/")
            books = Book.query()
            books = list(books)

        listTitle = {"isbn", "author", "avaliable", "type"}
        template_values = {

            "books": books,
            "listTitle": listTitle,
            "titleView": "Libros disponibles",
            "user": user.email(),
            "access_link": access_link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("list.html", **template_values))


app = webapp2.WSGIApplication([
    ('/seeBooks', seeBooks),
], debug=True)