# Gets book info from LABIRINT.RU
# TODO: write function where url is passed and other stuff performed


import requests
import re
from bs4 import BeautifulSoup

# EXAMPLE LINKS:
#url = 'https://www.labirint.ru/books/223752/'

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

def get_book_info(url):
    # def wrapper(*args, **kwargs):
    #     return orig_func(*args, **kwargs)
    # return wrapper
    return get_title(), get_author_name(), get_num_pages()


def get_title():
    # get title name
    title_info = soup.find('span', {'class': 'only_desc'}).get_text()
    title = title_info.split('"')[1]
    return title


def get_author_name():
    # get full author name
    authors_info = soup.find('div', {'class': 'authors'}).get_text()
    author = authors_info[7:].split(' ')
    return author


def get_num_pages():
    # get number of pages
    num_pages_info = soup.find('div', {'class': 'pages2'}).get_text()
    num_pages_regex = re.compile(r'Страниц: (\d+)')
    num_pages = num_pages_regex.search(num_pages_info).group(1)
    return num_pages

print(get_book_info(url))

# THIS IS WHAT I NEED THE DAMN THING TO DO
# def get_book_info(url):
#     res = requests.get(url)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     get_num_pages()
#     get_author_name()
#     get_title()
