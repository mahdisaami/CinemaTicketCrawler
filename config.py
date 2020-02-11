from peewee import MySQLDatabase
from models.local_config import MY_DATABASE


def connect_mysql():
    return MySQLDatabase('cinama', **MY_DATABASE)
