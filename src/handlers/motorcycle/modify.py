import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from src.model.appinfo import AppInfo
from src.model.motorcycle import Motorcycle


class ModifyMotorcycle(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['motorcycle_id']
        except:
            self.redirect("/error?msg=Motorcycle not found")
            return

        user = users.get_current_user()

        if user:
            user_name = user.nickname()
            access_link = users.create_logout_url("/")

            try:
                motorcycle = ndb.Key(urlsafe = id).get()
            except:
                self.redirect("/error?msg=Key don't exist")
                return

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "motorcycle": motorcycle,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("motorcycle_modify.html", **template_values))

        else:
            self.redirect("/")


    def post(self):
        try:
            id = self.request.GET['motorcycle_id']
        except:
            id = None

        if not id:
            self.redirect("/error?msg=Key don't exist")
            return

        user = users.get_current_user()


        if user:
            try:
                motorcycle = ndb.Key(urlsafe=id).get()
            except:
                self.redirect("/error?msg=Key don't exist")
                return

            motorcycle.model = self.request.get("model", "").strip()
            motorcycle.brand = self.request.get("brand", "").strip()
            motorcycle.user = self.request.get("user", "").strip()
            motorcycle.registration = self.request.get("registration", "").strip()
            motorcycle.comments = self.request.get("comments", "").strip()

            motorcycle.update()
            self.redirect("/index")
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ("/motorcycles/modify", ModifyMotorcycle),
], debug=True)