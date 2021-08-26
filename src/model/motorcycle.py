from google.appengine.ext import ndb

from src.model.client import Client


class Motorcycle(ndb.Model):
    client_key = ndb.KeyProperty(kind=Client)
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    registration = ndb.StringProperty(required=True, indexed=True)
    brand = ndb.StringProperty(required=True, indexed=True)
    model = ndb.StringProperty(required=True, indexed=True)
    comments = ndb.TextProperty()



