import bs4


DEFAULT_PARSER = 'html.parser'


def get_html_structure(webpage_source_code):
    soup = bs4.BeautifulSoup(webpage_source_code, DEFAULT_PARSER)
    print(soup.prettify())