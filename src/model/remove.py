from google.appengine.ext import ndb


@ndb.transactional(propagation=ndb.TrasactionOptions.INDEPENDENT)
def remove_client(cli_key):
    """
    Delete the client
    :param cli_key: The client key
    """
    cli_key.delete()


@ndb.transactional(propagation=ndb.TrasactionOptions.INDEPENDENT)
def remove_motorcycle(motor_key):
    """
    Delete the client
    :param cli_key: The client key
    """
    motor_key.delete()

@ndb.transactional(propagation=ndb.TrasactionOptions.INDEPENDENT)
def remove_repair(rep_key):
    """
    Delete the client
    :param cli_key: The client key
    """
    rep_key.delete()