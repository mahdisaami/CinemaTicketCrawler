import logging

file_logger = logging.getLogger(__name__)
file_logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler(filename="crawl.log")
f_handler.setLevel(logging.DEBUG)

f_formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s]: %("
                                "massage)s")
f_handler.formatter = f_formatter

file_logger.addHandler(f_handler)
