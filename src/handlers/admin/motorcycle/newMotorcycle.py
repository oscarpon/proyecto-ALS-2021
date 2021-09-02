import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.motorcycle import Motorcycle
from model.client import Client


class AdminAddMotorcycleHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
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
                                "client": client,
                                "motorcycles": motorcycles,
                                "logout": logout
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/admin/motorcycle/newMotorcycle.html", **template_values))
                        else:
                            msg = "Error al acceder al contenido del cliente"
                            volver = "/admin/showClients"

                            template_values = {
                                "msg": msg,
                                "volver": volver
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error al acceder al contenido del cliente"
                        volver = "/admin/showClients"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error al acceder al contenido del cliente"
                    volver = "/admin/showClients"

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

    def post(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                id_client = self.request.get("edIdClient", "Error")
                registration = self.request.get("edRegistration", "Error")
                brand = self.request.get("edBrand", "Error")
                model = self.request.get("edModel", "Error")
                comments = self.request.get("edComments", "Error")

                client = ndb.Key(urlsafe=id_client).get()
                motorcycle = Motorcycle(id_client=client.key, registration=registration, brand=brand, model=model, comments=comments)
                motorcycle.put()

                volver = "/admin/showClients"
                msg = "La motocycleta se ha creado correctamente"
                template_values = {
                    "volver": volver,
                    "msg": msg
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("mensajeGenerico.html", **template_values))
            else:
                self.redirect("/")
                return
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/admin/newMotorcycle', AdminAddMotorcycleHandler),
], debug=True)





