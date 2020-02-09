from parser import parse_html


def store_data(response, mysql=True):
    print(response.url)
    if mysql:
        save_data_to_mysql(response)


def save_data_to_mysql(response):
    parse_html(response.text)
