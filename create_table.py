from config import connect_mysql
from models.cinema import Cinema
from models.movie import Movie
from models.sans import Sans


def create_table():
    db = connect_mysql()
    CinemaMovie = Cinema.movie.get_through_model()
    db.create_tables([Cinema, Movie,
                      CinemaMovie, Sans])
