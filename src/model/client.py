from google.appengine.ext import ndb


class Client(ndb.Model):
    added = ndb.DateProperty(auto_now_add=True)
    user = ndb.StringProperty(required=True, indexed=True)
    dni = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True, indexed=True)
    surname = ndb.StringProperty(required=True, indexed=True)
    phone = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)


@ndb.transactional
def update(client):
    """
    Updates a client
    :param client: Client to client
    :return:  Client key.
    """
    return client.put()
