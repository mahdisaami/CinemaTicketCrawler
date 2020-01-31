from peewee import CharField, SmallIntegerField, DateField
from models.base import BaseModel


class Movie(BaseModel):
    name = CharField(null=True)
    type_movie = CharField(null=True)
    time_movie = CharField(null=True)
    rate = SmallIntegerField(null=True)
    vote_numbers = SmallIntegerField(null=True)
    date_start = DateField(null=True)
    director = CharField(null=True)
    actors = CharField(null=True)
