# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataCheckerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Dataset(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    organization = scrapy.Field()
