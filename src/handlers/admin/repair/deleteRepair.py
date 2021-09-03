import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.repair import Repair


class AdminDeleteRepairHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if users.is_current_user_admin():
                try:
                    id_repair = self.request.GET["id_repair"]
                except:
                    id_repair = "Error"
                if id_repair != "Error":
                    try:
                        repair = ndb.Key(urlsafe=id_repair).get()

                        logout = users.create_logout_url("/")
                        template_values = {
                            "repair": repair,
                            "logout": logout
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/admin/repair/deleteRepair.html", **template_values))
                    except:
                        msg = "Error inesperado 1"
                        volver = "/admin/showRepairs"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error inesperado 1"
                    volver = "/admin/showRepairs"

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
                id_repair = self.request.get("edIdRepair", "Error")
                if id_repair == "Error":
                    self.redirect("/")
                    return
                else:
                    try:
                        repair = ndb.Key(urlsafe=id_repair).get()

                        volver = "/admin/showMotorcycles"
                        msg = "La moto se ha sido eliminado correctamente"
                        repair.key.delete()

                        template_values = {
                            "volver": volver,
                            "msg": msg
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error inesperado 3"
                        volver = "/admin/showRepairs"

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
    ('/admin/deleteRepair', AdminDeleteRepairHandler),
], debug=True)
