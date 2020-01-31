import requests
from bs4 import BeautifulSoup

from mysql import save_cinemas, save_movies, save_sans


def parse_html(data):
    soup = BeautifulSoup(data)
    cinema = parse_cinema(data)
    save_cinemas(cinema)
    td = soup.find_all("td")
    for tag in td:
        link = extract_link(tag)
        response = requests.get(link)
        movie = parse_movie(response.text)
        save_movies(movie)
        sans_list = parse_sans(tag)
        if sans_list:
            save_sans(sans_list)


def extract_link(data):
    a = data.find("a")
    complete_link = "https://cinematicket.org" + a.attrs.get("href", "")
    return complete_link


def parse_sans(data):
    sans_data = dict(date=None, name_saloon=None, price=None, time=None,
                     is_available=False, url=None, movie=None, cinema=None)
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
        movie_data["type_movie"] = type_movie_tag.text

    time_movie_tag = soup.select_one(
        "body > section > section.movie-page.mtop > "
        "section > div > div > section > div > "
        "header > div.header_detail > div > "
        "div.col--small-12.col--medium-9.col--large"
        "-9.col-vertical-align_bottom > div > "
        "div:nth-child(2) > span:nth-child(3)")
    if time_movie_tag is not None:
        movie_data["time_movie"] = time_movie_tag.text

    rate_tag = soup.select_one("#ShowRating > span:nth-child(2)")
    if rate_tag is not None:
        movie_data["rate"] = rate_tag.text

    vote_numbers_tag = soup.select_one(
        '#ShowRating > small > span.movie-icon-num')
    if vote_numbers_tag is not None:
        movie_data["vote_numbers"] = vote_numbers_tag.text

    date_start_tag = soup.select_one(
        "body > section > section.movie-page.mtop > "
        "section > div > div > section > div > "
        "section.movie-wrap_section > div > "
        "div.col--small-12.col--medium-4.movie"
        "-wrap_col > figure:nth-child(4) > p")
    if date_start_tag is not None:
        movie_data["date_start"] = date_start_tag.text

    director = soup.select_one("body > section > section.movie-page.mtop > "
                               "section > div > div > section > div > header "
                               "> div.header_detail > div > "
                               "div.col--small-12.col--medium-9.col--large-9"
                               ".col-vertical-align_bottom > div > "
                               "div:nth-child(3) > div > div:nth-child(1) > "
                               "span")
    if director is not None:
        movie_data["director"] = director.text

    actors = soup.select_one("body > section > section.movie-page.mtop > "
                             "section > div > div > section > div > "
                             "section.movie-wrap_section > div > "
                             "div.col--small-12.col--medium-4.movie-wrap_col "
                             "> figure:nth-child(1) > p")
    if actors is not None:
        movie_data["actors"] = actors.text

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
        name_address["address"] = address_tag.text
    return name_address
