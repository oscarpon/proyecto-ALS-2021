from google.appengine.ext import ndb
from google.appengine.api import users
from webapp2_extras import jinja2
import webapp2

from src.model.appinfo import AppInfo
from src.model import remove
from src.model.repair import Repair

class DeleteRepair(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['repair_id']
        except:
            id = None

        if not id:
            self.redirect("/error?msg=Not found for delete")
            return

        user = users.get_current_user()

        if user:
            user_name = user.nickname()
            access_link = users.create_logout_url("/")

            try:
                repair = ndb.Key(urlsafe=id).get()
            except:
                self.redirect("/error?msg=Key not found")
                return

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "repair": repair
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("delete_motorcycle.html", **template_values));
        else:
            self.redirect("/")

    def post(self):
        try:
            id = self.request.GET['repair_id']
        except:
            self.redirect("/error?msg=Key not found")
            return

        user = users.get_current_user()

        if user and id:
            try:
                repair = ndb.Key(urlsafe=id).get()
            except:
                self.redirect("/error?msg=Key not found")
                return

            self.redirect("/info?msg=Motorcycle deleted")

            remove.remove_repair(repair.key)

        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ("/repair/delete", DeleteRepair),
], debug=True)