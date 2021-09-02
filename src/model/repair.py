from google.appengine.ext import ndb


class Repair(ndb.Model):
    added = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    id_motorcycle = ndb.KeyProperty(required=True)
    piece = ndb.StringProperty(required=True, indexed=True)
    price = ndb.StringProperty(required=True)
    comments = ndb.StringProperty()

