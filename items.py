# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# test
from scrapy.item import Item,Field


class SgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 哈哈哈哈哈哈
    title = Field()
    url = Field()
    body = Field()
