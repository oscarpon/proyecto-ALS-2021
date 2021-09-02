import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.client import Client
from model.motorcycle import Motorcycle


class ShowMotorcyclesHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        motorcycles = Motorcycle.query()
        if user:
            if not users.is_current_user_admin():
                user_name = user.nickname()
                clients = Client.query()
                client_names = []
                for motorcycle in motorcycles:
                    for client in clients:
                        if client.key == motorcycle.id_client:
                            client_names.append(client.name)

                logout = users.create_logout_url("/")
                template_values = {
                    "user_name": user_name,
                    "motorcycles": motorcycles,
                    "logout": logout,
                    "client_names": client_names
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("/usuario/motorcycle/showMotorcycles.html", **template_values))

            else:
                self.redirect("/")
                return
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/showMotorcycles', ShowMotorcyclesHandler),
], debug=True)
