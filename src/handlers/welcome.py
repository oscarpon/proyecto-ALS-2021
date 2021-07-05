import webapp2
import os
from webapp2_extras import jinja2
from google.appengine.api import users

from src.model.appinfo import AppInfo


class Welcome(webapp2.RequestHandler):
    def get(self):
        user_name = "login"
        user = users.get_current_user()

        if user:
            self.redirect("/manage_client")
            return
        else:
            access_link = users.create_login_url("/manage_client")

        template_values = {
            "info": AppInfo,
            "user_name": user_name,
            "access_link": access_link
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **template_values))


app = webapp2.WSGIApplication([
    ('/', Welcome),
], debug=True)
