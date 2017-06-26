import bs4
import src.definitions


def get_html_structure(webpage_source_code):
    soup = bs4.BeautifulSoup(webpage_source_code, src.definitions.DEFAULT_PARSER)
    print(soup.prettify())