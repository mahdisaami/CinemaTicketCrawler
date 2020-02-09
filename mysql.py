from models.cinema import Cinema
from models.link import Link
from models.movie import Movie
from models.sans import Sans

cinema_url_list = ['https://cinematicket.org/Location/Detail/?cid=304',
                   'https://cinematicket.org/Location/Detail/?cid=575',
                   'https://cinematicket.org/Location/Detail/?cid=448',
                   'https://cinematicket.org/Location/Detail/?cid=450',
                   'https://cinematicket.org/Location/Detail/?cid=524',
                   'https://cinematicket.org/Location/Detail/?cid=489',
                   'https://cinematicket.org/Location/Detail/?cid=429',
                   'https://cinematicket.org/Location/Detail/?cid=593',
                   'https://cinematicket.org/Location/Detail/?cid=344',
                   'https://cinematicket.org/Location/Detail/?cid=71',
                   'https://cinematicket.org/Location/Detail/?cid=546',
                   'https://cinematicket.org/Location/Detail/?cid=352',
                   'https://cinematicket.org/Location/Detail/?cid=89',
                   'https://cinematicket.org/Location/Detail/?cid=36',
                   'https://cinematicket.org/Location/Detail/?cid=73',
                   'https://cinematicket.org/Location/Detail/?cid=431',
                   'https://cinematicket.org/Location/Detail/?cid=72',
                   'https://cinematicket.org/Location/Detail/?cid=485',
                   'https://cinematicket.org/Location/Detail/?cid=445',
                   'https://cinematicket.org/Location/Detail/?cid=266',
                   'https://cinematicket.org/Location/Detail/?cid=396',
                   'https://cinematicket.org/Location/Detail/?cid=35',
                   'https://cinematicket.org/Location/Detail/?cid=522',
                   'https://cinematicket.org/Location/Detail/?cid=34',
                   'https://cinematicket.org/Location/Detail/?cid=81',
                   'https://cinematicket.org/Location/Detail/?cid=262',
                   'https://cinematicket.org/Location/Detail/?cid=417',
                   'https://cinematicket.org/Location/Detail/?cid=39',
                   'https://cinematicket.org/Location/Detail/?cid=61',
                   'https://cinematicket.org/Location/Detail/?cid=424',
                   'https://cinematicket.org/Location/Detail/?cid=51',
                   'https://cinematicket.org/Location/Detail/?cid=487',
                   'https://cinematicket.org/Location/Detail/?cid=427',
                   'https://cinematicket.org/Location/Detail/?cid=56',
                   'https://cinematicket.org/Location/Detail/?cid=50',
                   'https://cinematicket.org/Location/Detail/?cid=449',
                   'https://cinematicket.org/Location/Detail/?cid=115',
                   'https://cinematicket.org/Location/Detail/?cid=70',
                   'https://cinematicket.org/Location/Detail/?cid=48',
                   'https://cinematicket.org/Location/Detail/?cid=558',
                   'https://cinematicket.org/Location/Detail/?cid=722',
                   'https://cinematicket.org/Location/Detail/?cid=32',
                   'https://cinematicket.org/Location/Detail/?cid=83',
                   'https://cinematicket.org/Location/Detail/?cid=706',
                   'https://cinematicket.org/Location/Detail/?cid=88',
                   'https://cinematicket.org/Location/Detail/?cid=142',
                   'https://cinematicket.org/Location/Detail/?cid=98',
                   'https://cinematicket.org/Location/Detail/?cid=52',
                   'https://cinematicket.org/Location/Detail/?cid=43',
                   'https://cinematicket.org/Location/Detail/?cid=120',
                   'https://cinematicket.org/Location/Detail/?cid=414',
                   'https://cinematicket.org/Location/Detail/?cid=64',
                   'https://cinematicket.org/Location/Detail/?cid=55',
                   'https://cinematicket.org/Location/Detail/?cid=33',
                   'https://cinematicket.org/Location/Detail/?cid=285',
                   'https://cinematicket.org/Location/Detail/?cid=94',
                   'https://cinematicket.org/Location/Detail/?cid=91',
                   'https://cinematicket.org/Location/Detail/?cid=476',
                   'https://cinematicket.org/Location/Detail/?cid=687'
                   ]


def save_movies(data):
    Movie.create(**data)


def save_cinemas(data):
    Cinema.create(**data)


def save_sans(data, cinema_id, movie_id, ):
    for sans in data:
        Sans.create(**sans, movie=movie_id, cinema=cinema_id)


def save_cinema_movie(movie_id, cinema_id):
    CinemaMovie = Cinema.movie.get_through_model()
    CinemaMovie.create(movie=movie_id, cinema=cinema_id)


def save_cinema_links():
    for link in cinema_url_list:
        Link.create(url=link)


def load_cinema_links():
    return Link.select()
