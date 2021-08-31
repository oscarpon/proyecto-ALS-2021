from google.appengine.ext import ndb


class Client(ndb.Model):
    dni = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True, indexed=True)
    surname = ndb.StringProperty(required=True, indexed=True)
    phone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)

