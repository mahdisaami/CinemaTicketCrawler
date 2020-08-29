from peewee import MySQLDatabase
from models.local_config import MY_DATABASE


def connect_mysql():
    return MySQLDatabase('CinemaTicketCrawler', **MY_DATABASE)
