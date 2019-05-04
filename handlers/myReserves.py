import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

import model.reserve as reserve_mgt


class myReserves(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:

            access_link = users.create_logout_url("/")
            books = reserve_mgt.getBooks(user.email())
            books = list(books)

        listTitle = {"Titulo","ISBN", "Author", "Tipo"}
        template_values = {
            "books": books,
            "listTitle": listTitle,
            "titleView": "Mis reservas",
            "user": user.email(),
            "access_link": access_link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("my_reserves.html", **template_values))


app = webapp2.WSGIApplication([
    ('/myReserves', myReserves),
], debug=True)