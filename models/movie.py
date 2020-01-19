from peewee import CharField, TimeField, SmallIntegerField, DateField
from models.base import BaseModel


class Movie(BaseModel):
    name = CharField(max_length=60)
    type_movie = CharField(max_length=60)
    time_movie = TimeField()
    rate = SmallIntegerField()
    number_of_comments = SmallIntegerField()
    date_start = DateField()
