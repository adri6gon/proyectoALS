
import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users




class WelcomePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.redirect("/seeBooks")
            return
        else:
            access_link = users.create_login_url("/seeBooks")

        template_values = {
            "user": "Iniciar sesion",
            "access_link": access_link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', WelcomePage),
], debug=True)

