import bs4
import src.definitions
import requests


URL = 'http://prodota.ru/forum'


def get_source_code(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre'}
    requests_object = requests.get(url, headers)
    source_code = requests_object.text
    return source_code

def get_html_structure(webpage_source_code):
    soup = bs4.BeautifulSoup(webpage_source_code, src.definitions.DEFAULT_PARSER)
    print(soup.prettify())


if __name__ == '__main__':
    source_code = get_source_code(URL)
    get_html_structure(source_code)
