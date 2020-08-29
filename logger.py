import logging

file_logger = logging.getLogger(__name__)
file_logger.setLevel(logging.DEBUG)

f_handler = logging.FileHandler(filename="crawl.log")
f_handler.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)

f_formatter = logging.Formatter("[%(asctime)s][%(levelname)s][%(name)s]: %("
                                "message)s")
f_handler.formatter = f_formatter
c_handler.formatter = f_formatter

file_logger.addHandler(f_handler)
file_logger.addHandler(c_handler)
