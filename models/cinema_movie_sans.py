from peewee import ForeignKeyField
from models.base import BaseModel
from models.cinema_movie import CinemaMovie
from models.sans import Sans


class CinemaMovieSans(BaseModel):
    cinema_movie = ForeignKeyField(CinemaMovie, backref='sans')
    sans = ForeignKeyField(Sans, backref='cinema_movie')
