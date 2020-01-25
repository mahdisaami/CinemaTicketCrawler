from mysql import save_movies, save_cinemas
from parser import parse_page


def store_data(response, mysql=True):
    print(response.url)
    if mysql:
        return save_data_to_mysql(response)


def save_data_to_mysql(response):
    movies, cinemas = parse_page(response.text)
    save_movies(movies)
    save_cinemas(cinemas)
