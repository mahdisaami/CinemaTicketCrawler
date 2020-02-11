import threading
from queue import Queue
from logger import file_logger
import requests

from mysql import load_cinema_links
from store import store_data

def crawl_site(url):
    response = requests.get(url)
    file_logger.info('requeste for link {} '.format(url))
    store_data(response)


def crawl(index, que):
    while que.qsize:
        q = que.get()
        file_logger.info("thread {} is getting {}".format(index, q))
        crawl_site(q)
        que.task_done()



# def crawl_page(url):
#     response = requests.get(url)
#     store_data(response)


if __name__ == "__main__":
    # crawl_site('https://cinematicket.org/Location/Detail/?cid=344')
    file_logger.debug('Crowl Started')
    cinema_links = load_cinema_links()
    file_logger.debug('links are Crowled')
    file_logger.debug('Qeue is started')
    queue = Queue()
    for link in cinema_links:
        file_logger.info('link {} Add Queue'.format(link.url))
        queue.put(link.url)

    threads_list = list()
    for i in range(3):
        x = threading.Thread(target=crawl, args=(i, queue,))
        threads_list.append(x)
        x.start()

    for thread in threads_list:
        thread.join()
    file_logger.debug('finish')
    print("finish")
