import itertools
import re
import requests
from bs4 import BeautifulSoup


__URL_TEMPLATE = 'http://www.componente-accesorii.ro/grupul_de_articole/5208520110-{}.htm'


def generate_search_page_tables():

    for index in itertools.count(1, 1):
        url = __URL_TEMPLATE.format(index)

        response = requests.get(url)
        if response.status_code == 404:
            break

        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find('h1', text=re.compile('.*Lista cu piese de schimb.*')).findNextSibling('table')
        yield table

def generate_shop_urls():

    for table in generate_search_page_tables():
        table_rows = table.findAll('tr', {'bgcolor': 'white'})

        for row in table_rows:
            cells = row.findAll('td')
            if re.findall('\bacrtic\b', cells[1].get_text(), re.I):
                url = cells[2].find('a')
                if url.has_attr('href'):
                    yield url['href']


def main():

    with open('urls.txt', 'w') as urls:
        for url in generate_shop_urls():
            urls.write(url)


if __name__ == '__main__':
    main()
