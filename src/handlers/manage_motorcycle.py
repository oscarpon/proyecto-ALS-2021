import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from src.model.appinfo import AppInfo
from src.model.motorcycle import Motorcycle


class MotorcycleManager(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            user_name = user.nickname()
            motorcycles = Motorcycle.query(Motorcycle.user == user.user_id()).order(-Motorcycle.added)
            access_link = users.create_logout_url("/")

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "motorcycles": motorcycles
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("motorcycles.html", **template_values))
        else:
            self.redirect("/")
            return

app = webapp2.WSGIApplication([
    ('/manage_motorcycles', MotorcycleManager),
], debug=True)
