# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BizcommunityItem(scrapy.Item):
    date = scrapy.Field()
    event = scrapy.Field()
    location = scrapy.Field()
    
class ElaItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()

class JournalItem(scrapy.Item):
    title = scrapy.Field()
    authors = scrapy.Field()
    # doi = scrapy.Field()
    # purpose = scrapy.Field()
    # design = scrapy.Field()
    # findings = scrapy.Field()
    # value = scrapy.Field()
