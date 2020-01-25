from models.cinema import Cinema
from models.movie import Movie


def save_movies(data):
    Movie.create(**data)


def save_cinemas(data):
    for cinema in data:
        Cinema.create(**cinema)
