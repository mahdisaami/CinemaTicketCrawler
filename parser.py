import requests
from bs4 import BeautifulSoup
from logger import file_logger
from models.cinema import Cinema
from models.movie import Movie
from mysql import save_cinemas, save_movies, save_sans, save_cinema_movie


def parse_html_and_save(data):
    file_logger.info('parser is started')
    soup = BeautifulSoup(data)
    td = soup.find_all("td")
    if td:
        cinema = parse_cinema(data)
        save_cinemas(cinema)
        for tag in td:
            link = extract_link(tag)
            response = requests.get(link)
            movie = parse_movie(response.text)
            save_movies(movie)
            cinema_id = Cinema.get(Cinema.name == cinema["name"]).id
            movie_id = Movie.get(Movie.name == movie["name"]).id
            save_cinema_movie(movie_id, cinema_id)
            sans_list = parse_sans(tag)
            if sans_list:
                save_sans(sans_list, cinema_id, movie_id)
    else:
        file_logger.error('td is NUll')

def extract_link(data):
    a = data.find("a")
    complete_link = "https://cinematicket.org" + a.attrs.get("href", "")
    return complete_link


def parse_sans(data):
    sans_data = dict(date=None, name_saloon=None, price=None, time=None,
                     is_available=False, url=None)
    main_div = data.find("div", "showtime--panel")
    divs = main_div.find_all("div", "col--small-12 col--medium-12 "
                                    "col--large-12 col-vertical-align_top "
                                    "showtime--panel_box")
    sans_list = list()
    for div in divs:
        row = div.find("div", "row")
        sans = row.find_all("div", "col--small-6 col--medium-3 "
                                   "col-vertical-align_middle")
        for col in sans:
            a_tag = col.a
            if a_tag.attrs["href"] != "#":
                sans_data["is_available"] = True
                if div.header is not None:
                    sans_data["date"] = div.header.text.strip()
                sans_data["url"] = "https://cinematicket.org" + \
                                   a_tag.attrs["href"]
                spans = a_tag.find_all("span")
                if spans[0] is not None:
                    sans_data["time"] = spans[0].text.strip()
                if spans[1] is not None:
                    sans_data["name_saloon"] = spans[1].text.strip()
                if spans[2] is not None:
                    sans_data["price"] = spans[2].text.strip()
                sans_list.append(sans_data)
    # if len(sans_list) == 0:
    #     sans_list.append(sans_data)
    #     return sans_list
    return sans_list


def parse_movie(data):
    soup = BeautifulSoup(data)
    movie_data = dict(name=None, type_movie=None, time_movie=None,
                      rate=None, vote_numbers=None,
                      date_start=None, director=None, actors=None
                      )
    title_tag = soup.title
    if title_tag is not None:
        movie_data["name"] = title_tag.text

    type_movie_tag = soup.select_one(
        'body > section > section.movie-page.mtop >'
        ' section > div > div > section > div > '
        'header > div.header_detail > div > div.col'
        '--small-12.col--medium-9.col--large-9.col'
        '-vertical-align_bottom > div > div:nth-'
        'child(2) > span:nth-child(2)')
    if type_movie_tag is not None:
        movie_data["type_movie"] = type_movie_tag.text.strip()

    time_movie_tag = soup.select_one(
        "body > section > section.movie-page.mtop > "
        "section > div > div > section > div > "
        "header > div.header_detail > div > "
        "div.col--small-12.col--medium-9.col--large"
        "-9.col-vertical-align_bottom > div > "
        "div:nth-child(2) > span:nth-child(3)")
    if time_movie_tag is not None:
        movie_data["time_movie"] = time_movie_tag.text.strip()

    rate_tag = soup.select_one("#ShowRating > span:nth-child(2)")
    if rate_tag is not None:
        movie_data["rate"] = rate_tag.text.strip()
    else:
        rate_tag = soup.select_one("#rate > div:nth-child(1) > "
                                   "span:nth-child(2)")
        movie_data["rate"] = rate_tag.text.strip()

    vote_numbers_tag = soup.select_one(
        '#ShowRating > small > span.movie-icon-num')
    if vote_numbers_tag is not None:
        movie_data["vote_numbers"] = vote_numbers_tag.text.strip()
    else:
        vote_numbers_tag = soup.select_one("#rate > div:nth-child(1) > small "
                                           "> span.movie-icon-num")
        movie_data["vote_numbers"] = vote_numbers_tag.text.strip()

    date_start_tag = soup.select_one(
        "body > section > section.movie-page.mtop > "
        "section > div > div > section > div > "
        "section.movie-wrap_section > div > "
        "div.col--small-12.col--medium-4.movie"
        "-wrap_col > figure:nth-child(4) > p")
    if date_start_tag is not None:
        movie_data["date_start"] = date_start_tag.text.strip()

    director = soup.select_one("body > section > section.movie-page.mtop > "
                               "section > div > div > section > div > header "
                               "> div.header_detail > div > "
                               "div.col--small-12.col--medium-9.col--large-9"
                               ".col-vertical-align_bottom > div > "
                               "div:nth-child(3) > div > div:nth-child(1) > "
                               "span")
    if director is not None:
        movie_data["director"] = director.text.strip()
    # elif director is None: director = soup.select_one("body > section >
    # section > " "div.header.headerMotreb > div.container " ">
    # div.desFilm.desFilmMaskharebaz > p > " "span:nth-child(1)")
    # movie_data["director"] = director.text.replace("کارگردان:", "").strip()

    actors = soup.select_one("body > section > section.movie-page.mtop > "
                             "section > div > div > section > div > "
                             "section.movie-wrap_section > div > "
                             "div.col--small-12.col--medium-4.movie-wrap_col "
                             "> figure:nth-child(1) > p")
    if actors is not None:
        movie_data["actors"] = actors.text.strip()
    # elif actors is None:
    #     actors = soup.select_one("body > section > section > "
    #                              "div.header.headerMotreb > div.container > "
    #                              "div.desFilm.desFilmMaskharebaz > div > "
    #                              "div.iframe > div > p:nth-child(2)")
    #     movie_data["actors"] = actors.text.strip()

    return movie_data


def parse_cinema(data):
    soup = BeautifulSoup(data)
    name_address = dict(name=None, address=None)
    title_tag = soup.select_one("body > section > section > section > div "
                                "> div > section > div > header > div > "
                                "section > "
                                "div.relative.state-movie-zIndex > h1")
    if title_tag is not None:
        name_address['name'] = title_tag.text

    address_tag = soup.select_one("body > section > section > section > div "
                                  "> div > section > div > header > div > "
                                  "section > div.relative.state-movie-zIndex "
                                  "> h5")
    if address_tag is not None:
        name_address["address"] = address_tag.text.strip()
    return name_address
