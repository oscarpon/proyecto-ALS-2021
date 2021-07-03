from google.appengine.ext import ndb


class Repair(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True, indexed=True)
    motorcycle = ndb.StringProperty(required=True, indexed=True)
    piece = ndb.StringProperty(required=True, indexed=True)
    price = ndb.StringProperty(required=True)
    comments = ndb.StringProperty()


@ndb.transactional
def update(repair):
    """
    Updates a repair
    :param repair: The repair to repair.
    :return: The repair key.
    """
    return repair.put()