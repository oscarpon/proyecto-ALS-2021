import webapp2
from google.appengine.ext import ndb
from google.appengine.api import users

import src.model.motorcycle
from src.model.motorcycle import Motorcycle

class AddMotorcycle(webapp2.RequestHandler):
    def get(self):
        try:
            id = self.request.GET['client_id']
        except:
            self.redirect("/error?msg=missing client_id")
            return

        user = users.get_current_user()

        if user:
            try:
                client = ndb.Key(urlsafe=id).get()
            except:
                self.redirect("/error?msg=Error")
                return

            motorcycle = Motorcycle()
            motorcycle.user = client.key.id()
            motorcycle.model = "Tracer"
            motorcycle.brand = "Yamaha"
            motorcycle.registration = "5652LJB"
            motorcycle.comments = "Sin comentarios"
            key = motorcycle.update(motorcycle)
            self.redirect("/motorcycles/modify?client_id=" + client.key.urlsafe() + "&motorcycle_id" + key.urlsafe())

        else:
            self.redirect("/")

        return

app = webapp2.WSGIApplication([
    ("/motorcycle/add", AddMotorcycle),
], debug=True)