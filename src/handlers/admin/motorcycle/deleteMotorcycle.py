import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.motorcycle import Motorcycle


class AdminDeleteMotorCycleHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                try:
                    id_motorcycle = self.request.GET["id_motorcycle"]
                except:
                    id_motorcycle = "Error"
                if id_motorcycle != "Error":
                    try:
                        motorcycle = ndb.Key(urlsafe=id_motorcycle).get()

                        logout = users.create_logout_url("/")
                        template_values = {
                            "motorcycle": motorcycle,
                            "logout": logout
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/admin/motorcycle/deleteMotorcycle.html", **template_values))
                    except:
                        msg = "Error inesperado 1"
                        volver = "/admin/showMotorcycles"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error inesperado 1"
                    volver = "/admin/showMotorcycles"

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
                id_motorcycle = self.request.get("edIdMotorcycle", "Error")
                if id_motorcycle == "Error":
                    self.redirect("/")
                    return
                else:
                    try:
                        motorcycle = ndb.Key(urlsafe=id_motorcycle).get()

                        volver = "/admin/showMotorcycles"
                        msg = "La moto se ha sido eliminado correctamente"
                        motorcycle.key.delete()

                        template_values = {
                            "volver": volver,
                            "msg": msg
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error inesperado 3"
                        volver = "/admin/showMotorcycles"

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
    ('/admin/deleteMotorcycle', AdminDeleteMotorCycleHandler),
], debug=True)

