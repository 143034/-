# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    Confirmed = scrapy.Field()
    Suspected = scrapy.Field()
    Healing = scrapy.Field()
    Death = scrapy.Field()
    Deadline = scrapy.Field()
class Pro_ProjectItem(scrapy.Item):
    province_Name = scrapy.Field()
    province_Confirmed = scrapy.Field()
    province_Healing = scrapy.Field()
    province_Death = scrapy.Field()