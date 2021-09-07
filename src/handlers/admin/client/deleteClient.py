import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.motorcycle import Motorcycle


class AdminDeleteClientHandler(webapp2.RequestHandler):
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
                        self.response.write(jinja.render_template("/admin/client/deleteClient.html", **template_values))
                    except:
                        msg = "Error inesperado"
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
                if id_client == "Error":
                    self.redirect("/")
                    return
                else:
                    try:
                        client = ndb.Key(urlsafe=id_client).get()
                        client_motorcycles = Motorcycle.query(Motorcycle.id_client == client.key)

                        volver = "/admin/showClients"
                        msg = "El cliente y todos sus registros se han sido eliminado correctamente"
                        client.key.delete()
                        for motorcycle in client_motorcycles:
                            motorcycle.key.delete()
                        template_values = {
                            "volver": volver,
                            "msg": msg
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("mensajeGenerico.html", **template_values))
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
    ('/admin/deleteClient', AdminDeleteClientHandler),
], debug=True)