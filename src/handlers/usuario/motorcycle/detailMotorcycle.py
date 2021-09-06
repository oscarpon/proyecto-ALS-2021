import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb
from model.repair import Repair
from model.motorcycle import Motorcycle


class UserMotorcycleDetailHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            if not users.is_current_user_admin():
                try:
                    id_motorcycle = self.request.GET["id_motorcycle"]
                except:
                    id_motorcycle = "Error"
                if id_motorcycle != "Error":
                    try:
                        motorcycle = ndb.Key(urlsafe=id_motorcycle).get()
                        if motorcycle:
                            user_name = user.nickname()
                            repairs = Repair.query(Repair.id_motorcycle == motorcycle.key)
                            logout = users.create_logout_url("/")
                            template_values = {
                                "user_name": user_name,
                                "repairs": repairs,
                                "motorcycle": motorcycle,
                                "logout": logout
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(
                                jinja.render_template("/usuario/client/detailMotorcycle.html", **template_values))
                        else:
                            msg = "Error al acceder a la moto 1"
                            volver = "/usuario/showMotorcycles"

                            template_values = {
                                "msg": msg,
                                "volver": volver
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error al acceder a la moto 2"
                        volver = "/usuario/showMotorcycles"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error al acceder a la moto 3"
                    volver = "/usuario/showMotorcycles"

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
    ('/detailMotorcycle', UserMotorcycleDetailHandler),
], debug=True)