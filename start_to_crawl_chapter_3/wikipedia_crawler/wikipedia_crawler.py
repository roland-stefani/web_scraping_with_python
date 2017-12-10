from urllib.parse import urljoin
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


_BASE_URL = 'http://en.wikipedia.org'
pages = set()


def get_links(page_url):
    global pages
    try:
        html = urlopen(_BASE_URL + page_url)
        soup = BeautifulSoup(html, 'lxml')
        for link in soup.findAll('a', href=re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    # We have encountered a new page
                    new_page = link.attrs['href']
                    print(new_page)
                    pages.add(new_page)
                    get_links(new_page)
    except:
        pages.remove(page_url)

get_links('')