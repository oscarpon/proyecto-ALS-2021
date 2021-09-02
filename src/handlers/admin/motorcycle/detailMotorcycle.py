import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb


class AdminDetailMotorcycleHandler(webapp2.RequestHandler):
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
                            self.response.write(jinja.render_template("/admin/motorcycle/detailMotorcycle.html", **template_values))
                        else:
                            msg = "Error al acceder a la motocicleta 1"
                            volver = "/admin/showMotorcycles"

                            template_values = {
                                "msg": msg,
                                "volver": volver
                            }

                            jinja = jinja2.get_jinja2(app=self.app)
                            self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                    except:
                        msg = "Error al acceder al client 2"
                        volver = "/admin/showMotorcycles"

                        template_values = {
                            "msg": msg,
                            "volver": volver
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))
                else:
                    msg = "Error al acceder al client 3"
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
    ('/admin/detailMotorcycle', AdminDetailMotorcycleHandler),
], debug=True)