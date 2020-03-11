import scrapy
from ..items import BizcommunityItem


class BizcommSpider(scrapy.Spider):
    name = 'bizcomm_spider'
    start_urls = ['https://www.bizcommunity.africa/Events/410/362.html']

    def parse(self, response):
        items = BizcommunityItem()

        for detail in response.css("tr"):
            date= detail.css("td:first-child::text").extract()
            event = detail.css("td:nth-child(2) a::text").extract()
            location = detail.css("td:last-child::text").extract()

            items['date'] = date
            items['event']= event
            items['location'] = location
            yield items

            next_page = response.css(".button-next.large.kRound::attr(href)")
            if next_page:
                url = response.urljoin(next_page[0].extract())
                yield scrapy.Request(url, self.parse)
