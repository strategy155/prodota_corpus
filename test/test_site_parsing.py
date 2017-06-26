import bs4
import src.definitions
import requests


URL = 'http://prodota.ru/forum'


def get_source_code(url):
    requests_object = requests.get(url)
    source_code = requests_object.text
    print(requests_object.content)
    return source_code

def get_html_structure(webpage_source_code):
    soup = bs4.BeautifulSoup(webpage_source_code, src.definitions.DEFAULT_PARSER)
    print(soup.prettify())


if __name__ == '__main__':
    source_code = get_source_code(URL)
    get_html_structure(source_code)
