from models.cinema import Cinema
from models.movie import Movie
from models.sans import Sans


def save_movies(data):
    Movie.create(**data)


def save_cinemas(data):
    Cinema.create(**data)


def save_sans(data):
    for sans in data:
        Sans.create(**sans)
