import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.motorcycle import Motorcycle
from model.repair import Repair
from datetime import datetime


class AdminAddRepairHandler(webapp2.RequestHandler):
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
                        if motorcycle:
                            user_name = user.nickname()
                            logout = users.create_logout_url("/")
                            template_values = {
                                "user_name": user_name,
                                "motorcycle": motorcycle,
                                "logout": logout
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/admin/repair/newRepair.html", **template_values))
                        else:
                            msg = "Error al acceder al contenido del vehiculo"
                            volver = "/admin/showMotorcycles"

                            template_values = {
                                "msg": msg,
                                "volver": volver
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error al acceder al contenido del vehiculo"
                        volver = "/admin/showMotorcycles"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error al acceder al contenido del vehiculo"
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
                #added = self.request.get("edAdded", "Error")
                piece = self.request.get("edPiece", "Error")
                price = self.request.get("edPrice", "Error")
                comments = self.request.get("edComments", "Error")

                motorcycle = ndb.Key(urlsafe=id_motorcycle).get()
                repair = Repair(id_motorcycle=motorcycle.key, piece=piece, price=price, comments=comments)
                repair.put()

                volver = "/admin/detailMotorcycle?id_motorcycle="
                msg = "La reparacion se ha creado correctamente"
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
    ('/admin/newRepair', AdminAddRepairHandler),
], debug=True)