import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb

from src.model.appinfo import AppInfo
from src.model.motorcycle import Motorcycle
from src.model.repair import Repair

class RepairManager(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            user_name = user.nickname()

            try:
                id = self.request.GET['motorcycle_id']

            except:
                id = None

            if not id:
                self.redirect("/error?msg_error=Key not found")
                return

            motorcycle = ndb.Key(urlsafe=id).get()
            repair = Repair.query(Repair.motorcycle == motorcycle.key.id()).order(Repair.piece)
            access_link = users.create_logout_url("/")

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "motorcycle": motorcycle,
                "repair": repair
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("reparaciones.html", **template_values))
        else:
            self.redirect("/")
            return

app = webapp2.WSGIApplication([
    ('/manage_repair', RepairManager),
], debug=True)