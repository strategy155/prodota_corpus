import bs4
import src.definitions
import requests


URL = 'http://prodota.ru/forum'
LINK_TAG_NAME = "a"


def get_source_code(url):
    requests_object = requests.get(url)
    source_code = requests_object.text
    print(requests_object.content)
    return source_code


def get_soup(html_source_code):
    soup = bs4.BeautifulSoup(html_source_code, src.definitions.DEFAULT_PARSER)
    return soup


def get_tags(tag_name, soup):
    tags = soup.find_all(tag_name)
    return tags


def main():
    source_code = get_source_code(URL)
    soup = get_soup(source_code)
    tags = get_tags(LINK_TAG_NAME, soup)
    print(tags)


if __name__ == '__main__':
    main()
