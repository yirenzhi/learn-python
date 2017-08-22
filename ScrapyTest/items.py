# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    bir = scrapy.Field()
    bio = scrapy.Field()
