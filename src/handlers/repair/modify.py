import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from src.model.appinfo import AppInfo
from src.model.repair import Repair


class ModifyRepair(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['repair_id']
        except:
            self.redirect("/error?msg=Repair not found")
            return

        user = users.get_current_user()

        if user:
            user_name = user.nickname()
            access_link = users.create_logout_url("/")

            try:
                repair = ndb.Key(urlsafe = id).get()
            except:
                self.redirect("/error?msg=Key don't exist")
                return

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "repair": repair,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("modify_repair.html", **template_values))

        else:
            self.redirect("/")


    def post(self):
        try:
            id = self.request.GET['repair_id']
        except:
            id = None

        if not id:
            self.redirect("/error?msg=Key don't exist")
            return

        user = users.get_current_user()


        if user:
            try:
                repair = ndb.Key(urlsafe=id).get()
            except:
                self.redirect("/error?msg=Key don't exist")
                return

            repair.piece = self.request.get("piece", "").strip()
            repair.price = self.request.get("price", "").strip()
            repair.comments = self.request.get("comments", "").strip()

            repair.update()
            self.redirect("/index")
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([
    ("/repair/modify", ModifyRepair),
], debug=True)