import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.client import Client


class AdminAddClientHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                logout = users.create_logout_url("/")
                template_values = {
                    "user_name": user.nickname(),
                    "logout": logout
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("/admin/client/newClient.html", **template_values))
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
                dni = self.request.get("edDni", "Error")
                name = self.request.get("edName", "Error")
                surname = self.request.get("edSurname", "Error")
                phone = self.request.get("edPhone", "Error")
                email = self.request.get("edEmail", "Error")

                try:
                    new_client = Client(dni=dni.lower(), name=name.capitalize(), surname=surname.capitalize(), phone=phone, email=email.lower())
                    new_client.put()

                    msg = "El cliente se ha creado correctamente"

                    volver = "/admin/showClients"

                    template_values = {
                        "msg": msg,
                        "volver": volver
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))

                except:
                    msg = "error al recuperar de la base de datos"

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


app = webapp2.WSGIApplication([
    ('/admin/newClient', AdminAddClientHandler),
], debug=True)

