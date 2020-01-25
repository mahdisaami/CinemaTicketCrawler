from peewee import ForeignKeyField
from models.base import BaseModel
from models.cinema import Cinema
from models.movie import Movie


class CinemaMovie(BaseModel):
    cinema = ForeignKeyField(Cinema, backref='movies')
    movie = ForeignKeyField(Movie, backref='cinemas')


