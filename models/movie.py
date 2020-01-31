from peewee import CharField, SmallIntegerField, DateField
from models.base import BaseModel


class Movie(BaseModel):
    name = CharField()
    type_movie = CharField()
    time_movie = CharField()
    rate = SmallIntegerField()
    vote_numbers = SmallIntegerField()
    date_start = DateField()
    director = CharField()
    actors = CharField()
