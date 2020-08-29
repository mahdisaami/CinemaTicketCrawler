from peewee import CharField, SmallIntegerField, DateField
from models.base import BaseModel


class Movie(BaseModel):
    name = CharField()
    type_movie = CharField(null=True)
    time_movie = CharField(null=True)
    rate = CharField(null=True)
    vote_numbers = SmallIntegerField(null=True)
    date_start = DateField(null=True)
    director = CharField(null=True)
    actors = CharField(null=True)

