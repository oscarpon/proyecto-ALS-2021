from google.appengine.ext import ndb

from src.model.client import Client
from src.model.motorcycle import Motorcycle
from src.model.repair import Repair


@ndb.transactional
def remove_client(cli_key):
    """
    Delete the client
    :param cli_key: The client key
    """
    cli_key.delete()


@ndb.transactional
def remove_motorcycle(motor_key):
    """
    Delete the client
    :param motor_key:
    :param cli_key: The client key
    """
    motor_key.delete()


@ndb.transactional
def remove_repair(rep_key):
    """
    Delete the client
    :param rep_key:
    :param cli_key: The client key
    """
    rep_key.delete()
