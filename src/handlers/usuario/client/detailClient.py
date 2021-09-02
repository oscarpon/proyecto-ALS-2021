import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.client import Client
from model.motorcycle import Motorcycle


class UserDetailClientHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if not users.is_current_user_admin():
                try:
                    id_client = self.request.GET["id_client"]
                except:
                    id_client = "Error"
                if id_client != "Error":
                    try:
                        client = ndb.Key(urlsafe=id_client).get()
                        if client:
                            user_name = user.nickname()
                            motorcycles = Motorcycle.query(Motorcycle.id_client == client.key)
                            logout = users.create_logout_url("/")
                            template_values = {
                                "user_name": user_name,
                                "motorcycles": motorcycles,
                                "client": client,
                                "logout": logout
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(
                                jinja.render_template("/usuario/client/detailClient.html", **template_values))
                        else:
                            msg = "Error al acceder al client 1"
                            volver = "/usuario/showClients"

                            template_values = {
                                "msg": msg,
                                "volver": volver
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error al acceder al client 2"
                        volver = "/usuario/showClients"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error al acceder al client 3"
                    volver = "/usuario/showClients"

                    template_values = {
                        "msg": msg,
                        "volver": volver
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
            else:
                self.redirect("/")
                return
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/detailClient', UserDetailClientHandler),
], debug=True)