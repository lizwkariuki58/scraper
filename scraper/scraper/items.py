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
    

