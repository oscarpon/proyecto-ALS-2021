from google.appengine.ext import ndb


class Motorcycle(ndb.Model):
    client = ndb.IntegerProperty(required=True, indexed=True)
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    registration = ndb.StringProperty(required=True, indexed=True)
    brand = ndb.StringProperty(required=True, indexed=True)
    model = ndb.StringProperty(required=True, indexed=True)
    comments = ndb.TextProperty()


@ndb.transactional
def update(motorcycle):
    """
    Update a motorcycle.
    :param motorcycle: The motorcycle to motorcycle.
    :return: Motorcycle key.
    """
    return motorcycle.put()
