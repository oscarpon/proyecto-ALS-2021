import webapp2
from webapp2_extras import jinja2

from src.model.appinfo import AppInfo


class InfoHandler(webapp2.RequestHandler):
    def get(self):
        try:
            msg = self.request.GET['msg']
            url = self.request.GET['url']

        except:
            msg = None
            url = "/"

        if not msg:
            self.redirect("error?msg=Not found")
            return

        template_values = {
            "msg": msg,
            "url": url,
            "info": AppInfo
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("info.html", **template_values))


app = webapp2.WSGIApplication([
    ("/info", InfoHandler),
], debug=True)