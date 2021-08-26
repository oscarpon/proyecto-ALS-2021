import webapp2
from google.appengine.api import users

import src.model.user
from src.model.client import Client

class AddClient(webapp2.RequestHandler):

   def get(self):

      user = users.get_current_user();

      if user:
         client = Client()
         client.user = user.user_id()
         client.name = "Nombre"
         client.email = "email@email.com"
         client.dni = "35324426W"
         client.phone = "615232063"
         client.surname = "Apellidos"
         key = src.model.user.update(client)
         self.redirect("/clients/modify?client_id=" + key.urlsafe())
      else:
         self.redirect("/")

      return


app = webapp2.WSGIApplication([
   ("/clients/add", AddClient),
], debug=True)






