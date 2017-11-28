# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #地铁 标题 小区 户型 面积 价格 发布时间 爬取时间 链接url
    subway = scrapy.Field()
    title = scrapy.Field()
    xiaoqu = scrapy.Field()
    huxing = scrapy.Field()
    area = scrapy.Field()
    price = scrapy.Field()
    release_time = scrapy.Field()
    crawling_time = scrapy.Field()
    url = scrapy.Field()
