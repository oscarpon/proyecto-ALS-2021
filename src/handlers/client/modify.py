import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import jinja2

from src.model.client import Client
from src.model.appinfo import AppInfo

class ModifyClient(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['client_id']
        except:
            self.redirect("/error?msg=Client not found")
            return

        user = users.get_current_user()

        if user:
            user_name = user.nickname()
            access_link = users.create_logout_url("/")

            try:
                client = ndb.Key(urlsafe = id).get()
            except:
                self.redirect("/error?msg=Key don't exist")
                return

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "client": client,
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("modify_client.html", **template_values))

        else:
            self.redirect("/")

    def post(self):
        try:
            id = self.request.GET['client_id']
        except:
            id = None

        if not id:
            self.redirect("/error?msg=Key don't exist")
            return

        user = users.get_current_user()


        if user:
            try:
                client = ndb.Key(urlsafe=id).get()
            except:
                self.redirect("/error?msg=Key don't exist")
                return

            client.dni = self.request.get("dni", "").strip()
            client.name = self.request.get("name", "").strip()
            client.surname = self.request.get("surname", "").strip()
            client.phone = self.request.get("phone", "").strip()
            client.email = self.request.get("email", "").strip()

            client.update()
            self.redirect("/index")
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ("/clients/modify", ModifyClient),
], debug=True)