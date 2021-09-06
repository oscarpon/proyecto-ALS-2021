import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from model.repair import Repair


class ShowRepairsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        repairs = Repair.query()
        if user:
            if not users.is_current_user_admin():
                user_name = user.nickname()

                logout = users.create_logout_url("/")
                template_values = {
                    "user_name": user_name,
                    "repairs": repairs,
                    "logout": logout
                }

                jinja = jinja2.get_jinja2(app=self.app)
                self.response.write(jinja.render_template("/usuario/repair/showRepairs.html", **template_values))

            else:
                self.redirect("/")
                return
        else:
            self.redirect("/")
            return


app = webapp2.WSGIApplication([
    ('/showRepairs', ShowRepairsHandler),
], debug=True)
