import scrapy
from scrapy.selector import Selector
from wiki_spider.items import Article


class ArticleSpider(scrapy.Spider):

    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/Salvator_Mundi_(Leonardo)',
        'https://en.wikipedia.org/wiki/Python_%28programming_language%29'
    ]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1[@id="firstHeading"]/text()')[0].extract()
        print('Title is: {}:'.format(title))
        item['title'] = title
        return item

