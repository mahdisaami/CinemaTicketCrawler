from peewee import Model, CharField

from config import connect_mysql


class Link(Model):
    url = CharField()

    class Meta:
        database = connect_mysql()
