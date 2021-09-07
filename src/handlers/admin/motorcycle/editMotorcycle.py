import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb


class AdminEditMotorcycleHandler(webapp2.RequestHandler):
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

                        user_name = user.nickname()
                        logout = users.create_logout_url("/")
                        template_values = {
                            "user_name": user_name,
                            "motorcycle": motorcycle,
                            "logout": logout
                        }

                        jinja = jinja2.get_jinja2(app=self.app)
                        self.response.write(jinja.render_template("/admin/motorcycle/editMotorcycle.html", **template_values))
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
                    msg = "Error inesperado 2"
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
                registration = self.request.get("edRegistration", "Error")
                brand  = self.request.get("edBrand", "Error")
                model = self.request.get("edModel", "Error")
                comments = self.request.get("edComments", "Error")

                try:
                    motorcycle = ndb.Key(urlsafe=id_motorcycle).get()
                    motorcycle.registration = registration.upper()
                    motorcycle.brand = brand.capitalize()
                    motorcycle.model = model.capitalize()
                    motorcycle.comments = comments
                    motorcycle.put()

                    volver = "/admin/showMotorcycles"
                    msg = "La moto ha sido editada correctamente"

                    template_values = {
                        "msg": msg,
                        "volver": volver
                    }

                    jinja = jinja2.get_jinja2(app=self.app)
                    self.response.write(jinja.render_template("/mensajeGenerico.html", **template_values))

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
    ('/admin/editMotorcycle', AdminEditMotorcycleHandler),
], debug=True)
