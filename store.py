from parser import parse_html_and_save


def store_data(response, mysql=True):
    if mysql:
        save_data_to_mysql(response)


def save_data_to_mysql(response):
    parse_html_and_save(response.text)
