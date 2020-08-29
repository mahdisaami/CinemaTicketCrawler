from peewee import CharField, TextField, ManyToManyField
from models.base import BaseModel
from models.movie import Movie


class Cinema(BaseModel):
    name = CharField()
    address = TextField()
    movie = ManyToManyField(Movie, backref="cinema")
