from google.appengine.ext import ndb
from google.appengine.api import users


class User(ndb.Model):

    user_id = ndb.StringProperty(required=True, indexed=True)
    name = ndb.StringProperty(required=True, indexed=True)
    is_admin = ndb.BooleanProperty(required=True, indexed=False)

    def __unicode__(self):
        return self.user_id + ' ' + self.name + " admin: " + str(self.is_admin)

    @staticmethod
    def get_current_user():
        toret = None
        gae_user = users.get_current_user()

        if(users.is_current_user_admin() or (gae_user and gae_user.email().lower().endswith("@esei.uvigo.es"))):
            try:
                located_user = User.query(User.user_id == gae_user.user_id()).fetch(1)

                if located_user:
                    toret = located_user[0]
                else:
                    print("Creando nuevo cliente")
                    toret = User()
                    toret.user_id = gae_user.user_id()
                    toret.name = gae_user.nickname()
                    toret.is_admin = users.is_current_user_admin()
                    toret.gae_user = gae_user

                    print("Client created")
                    toret.put()

            except Exception as e:
                print(e)

        return toret
