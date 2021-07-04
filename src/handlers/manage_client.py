import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users

from src.model.appinfo import AppInfo
from src.model.client import Client


class ClientManager(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            user_name = user.nickname()
            clients = Client.query(Client.user == user.user_id()).order(-Client.added)
            access_link = users.create_logout_url("/")

            template_values = {
                "info": AppInfo,
                "user_name": user_name,
                "access_link": access_link,
                "clients": clients
            }

            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(jinja.render_template("clients.html", **template_values))
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([('/manage_client', ClientManager), ], debug=True)