import scrapy
import time
from ..items import ElaItem

class ElaSpider(scrapy.Spider):
    name = 'ela_spider'
    start_urls = ['https://ela-newsportal.com/']

    def parse(self, response):
        items = ElaItem() 
        
        for article in response.css(".article"):
            title = article.css(".title a::text").extract()
            link = article.css(".title a::attr(href)").extract()
            date = article.css(".date::text").extract()

            items['title']= title
            items['link'] = link
            items['date'] = date
            yield items

            next_page = response.css(".next::attr(href)")
            if next_page:
                url = response.urljoin(next_page[0].extract())
                yield scrapy.Request(url, self.parse)
