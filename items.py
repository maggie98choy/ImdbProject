# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbprojectItem(scrapy.Item):
    # define the fields for your item here like:
    picture_title = scrapy.Field()
    genre = scrapy.Field()
    TotalNumByGenre = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    user_rating = scrapy.Field()
    outline = scrapy.Field()
    credit = scrapy.Field()
    pass
