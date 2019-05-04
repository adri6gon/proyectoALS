import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from model.book import Book


class showBook(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:

            access_link = users.create_logout_url("/")
            id = int(self.request.get("id"))
            book = Book.get_by_id(id)

        template_values = {
            "book": book,
            "titleView": "Ver en detalle",
            "user": user.email(),
            "access_link": access_link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("showBook.html", **template_values))


app = webapp2.WSGIApplication([
    ('/showBook', showBook),
], debug=True)