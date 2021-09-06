import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb


class AdminEditRepairHandler(webapp2.RequestHandler):
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

                        user_name = user.nickname()
                        logout = users.create_logout_url("/")
                        template_values = {
                            "user_name": user_name,
                            "repair": repair,
                            "logout": logout
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/admin/repair/editRepair.html", **template_values))
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
                    msg = "Error inesperado 2"
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
                piece = self.request.get("edPiece", "Error")
                price  = self.request.get("edPrice", "Error")
                comments = self.request.get("edComments", "Error")

                try:
                    repair = ndb.Key(urlsafe=id_repair).get()
                    repair.piece = piece
                    repair.price = price
                    repair.comments = comments
                    repair.put()

                    volver = "/admin/showRepairs"
                    msg = "La reparacion ha sido editada correctamente"

                    template_values = {
                        "msg": msg,
                        "volver": volver
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))

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
    ('/admin/editRepair', AdminEditRepairHandler),
], debug=True)