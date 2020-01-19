from config import connect_mysql
from models.actor import Actor
from models.cinema import Cinema
from models.cinema_movie import CinemaMovie
from models.cinema_movie_sans import CinemaMovieSans
from models.movie import Movie
from models.movie_actor import MovieActor
from models.sans import Sans


def create_table():
    db = connect_mysql()
    db.create_tables([Actor, MovieActor, Cinema, CinemaMovieSans, Movie,
                      CinemaMovie, Sans])

