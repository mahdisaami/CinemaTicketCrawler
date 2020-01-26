from bs4 import BeautifulSoup


def parse_html(data):
    soup = BeautifulSoup(data)
    row = soup.select_one(
        "body > section > section > div > div > section > section >"
        " section > section > div"
    )
    section_list = row.find_all("section")
    link_list = list()
    for section in section_list:
        link = extract_link(section)
        link_list.append(link)
    return link_list


def extract_link(data):
    a = data.find("a")
    complete_link = "https://cinematicket.org" + a.attrs.get("href", "")
    return complete_link


def parse_page(data):
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

    cinemas_tag = soup.find_all("tr")
    cinemas_list = list()
    for cinema in cinemas_tag:
        cinema_data = extract_cinema(cinema)
        cinemas_list.append(cinema_data)
    return movie_data, cinemas_list


def extract_cinema(data):
    name_address = dict(name=None, address=None)
    title_cinema = data.find("div", "movie__title")
    if title_cinema is not None:
        name_address['name'] = title_cinema.text

    address_tag = data.p
    if address_tag is not None:
        name_address["address"] = address_tag.text
    return name_address
