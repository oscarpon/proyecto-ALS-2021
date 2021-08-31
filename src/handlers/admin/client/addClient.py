import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from src.model.client import Client


class AdminAddClient(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                template_values = {
                    "user_name": user.nickname()
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
                    new_client = Client(dni=dni.lower(), name=name.upper(), surname=surname.upper(), phone=phone, email=email)
                    new_client.put()

                    url = "/admin/showClients"
                    msg = "El cliente se ha añadido correctamente"

                    template_values = {
                        "msg": msg,
                        "url": url
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/message.html", **template_values))
                except:
                    msg = "Error al recuperar de la base de datos"
                    url = "/admin/showClients"

                    template_values = {
                        "msg": msg,
                        "url": url
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/message.html", **template_values))

            else:
                self.redirect("/")
                return
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/admin/addClient', AdminAddClient),
], debug=True)
