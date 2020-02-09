from peewee import CharField, TimeField, \
    BooleanField, DateField, ForeignKeyField

from models.base import BaseModel
from models.cinema import Cinema
from models.movie import Movie


class Sans(BaseModel):
    date = DateField(null=True)
    name_saloon = CharField(null=True)
    price = CharField(null=True)
    time = TimeField(null=True)
    is_available = BooleanField(null=True)
    url = CharField(null=True)
    movie = ForeignKeyField(Movie, backref="sans", null=True)
    cinema = ForeignKeyField(Cinema, backref="sans", null=True)
