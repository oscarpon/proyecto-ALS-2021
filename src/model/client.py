from google.appengine.ext import ndb

from src.model.user import User


class Client(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    user_key = ndb.KeyProperty(kind=User)
    dni = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True, indexed=True)
    surname = ndb.StringProperty(required=True, indexed=True)
    phone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)