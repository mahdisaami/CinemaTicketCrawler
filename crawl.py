import requests

from store import store_data


def crawl_site(url):
    response = requests.get(url)
    store_data(response)


# def crawl_page(url):
#     response = requests.get(url)
#     store_data(response)


if __name__ == "__main__":
    crawl_site('https://cinematicket.org/Location/Detail/?cid=448')
