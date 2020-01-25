from peewee import CharField, SmallIntegerField, DateField
from models.base import BaseModel


class Movie(BaseModel):
    name = CharField(max_length=60)
    type_movie = CharField(max_length=60)
    time_movie = CharField()
    rate = SmallIntegerField()
    vote_numbers = SmallIntegerField()
    date_start = DateField()
    director = CharField(max_length=60)
