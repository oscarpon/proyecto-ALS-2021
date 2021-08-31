from google.appengine.ext import ndb

from src.model.motorcycle import Motorcycle


class Repair(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    id_motorcycle = ndb.KeyProperty(kind=Motorcycle, required=True)
    piece = ndb.StringProperty(required=True, indexed=True)
    price = ndb.StringProperty(required=True)
    comments = ndb.StringProperty()
