import requests

from parser import parse_html
from store import store_data


def crawl_site(url):
    response = requests.get(url)
    crawl = True
    while crawl:
        links = parse_html(response.text)
        for link in links:
            crawl_page(link)


def crawl_page(url):
    response = requests.get(url)
    crawl = True
    while crawl:
        store_data(response)


if __name__ == "__main__":
    crawl_site('https://cinematicket.org/Events/Films')
