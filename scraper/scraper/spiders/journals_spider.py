import scrapy
from scrapy_splash import SplashRequest
import time
from ..items import JournalItem

class  JournalSpider(scrapy.Spider):
    name = 'journal_spider'
    start_urls = ['https://www.emerald.com/insight/search?q=human+resource+africa&showAll=true']

    def parse(self, response):
        items = JournalItem()

        for article in response.css(".px-md-0"):
            title = article.css("h2 a::attr(title)").extract()
            authors = article.css(".my-3 a::text").extract()

            items['title'] = title
            items['authors'] = authors
            yield items