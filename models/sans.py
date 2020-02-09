from peewee import CharField, TimeField, \
    BooleanField, DateField, ForeignKeyField

from models.base import BaseModel
from models.cinema import Cinema
from models.movie import Movie


class Sans(BaseModel):
    date = DateField()
    name_saloon = CharField()
    price = CharField()
    time = TimeField()
    is_available = BooleanField()
    url = CharField()
    movie = ForeignKeyField(Movie, backref="sans")
    cinema = ForeignKeyField(Cinema, backref="sans")
