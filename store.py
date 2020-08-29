from parser import parse_html_and_save
from logger import file_logger


def store_data(response, mysql=True):
    if mysql:
        save_data_to_mysql(response)
    else:
        file_logger.error('sql connection failed')


def save_data_to_mysql(response):
    parse_html_and_save(response.text)
