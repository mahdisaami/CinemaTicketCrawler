from peewee import ForeignKeyField

from models.actor import Actor
from models.base import BaseModel
from models.movie import Movie


class MovieActor(BaseModel):
    actor = ForeignKeyField(Actor, backref='movies')
    movie = ForeignKeyField(Movie, backref='actors')
