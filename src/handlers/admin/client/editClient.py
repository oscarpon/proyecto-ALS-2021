import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb


class AdminEditClientHandler(webapp2.RequestHandler):
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

                        user_name = user.nickname()
                        logout = users.create_logout_url("/")
                        template_values = {
                            "user_name": user_name,
                            "client": client,
                            "logout": logout
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/admin/client/editClient.html", **template_values))
                    except:
                        msg = "Error inesperado 1"
                        volver = "/admin/showClients"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))

                else:
                    msg = "Error inesperado 2"
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
                dni = self.request.get("edDni", "Error")
                name = self.request.get("edName", "Error")
                surname = self.request.get("edSurname", "Error")
                phone = self.request.get("edPhone", "Error")
                email = self.request.get("edEmail", "Error")

                try:
                    client = ndb.Key(urlsafe=id_client).get()
                    client.dni = dni.lower()
                    client.name = name.capitalize()
                    client.surname = surname.capitalize()
                    client.phone = phone
                    client.email = email.lower()
                    client.put()

                    volver = "/admin/showClients"
                    msg = "El cliente ha sido editado correctamente"

                    template_values = {
                        "msg": msg,
                        "volver": volver
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))

                except:
                    msg = "Error inesperado 3"
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
    ('/admin/editClient', AdminEditClientHandler),
], debug=True)