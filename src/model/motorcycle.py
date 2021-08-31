from google.appengine.ext import ndb

from src.model.client import Client


class Motorcycle(ndb.Model):
    id_client = ndb.KeyProperty(required=True)
    registration = ndb.StringProperty(required=True, indexed=True)
    brand = ndb.StringProperty(required=True, indexed=True)
    model = ndb.StringProperty(required=True, indexed=True)
    comments = ndb.TextProperty()



