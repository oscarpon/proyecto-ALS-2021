import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from src.model.client import Client


class AdminShowClients(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                user_name = user.nickname()
                clients = Client.query()
                template_values = {
                    "user_name": user_name,
                    "clients": clients
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("/admin/client/showClients.html", **template_values))

            else:
                self.redirect("/")
                return
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/admin/showClients', AdminShowClients),
], debug=True)