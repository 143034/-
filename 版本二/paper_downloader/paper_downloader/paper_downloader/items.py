# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


# 创建保存爬取ACM结果的容器
class PaperItem(Item):
    collection = table = 'papers'  # 数据表
    title = Field()  # 题目
    authors = Field()  # 作者
    publicationDate = Field()  # 出版日期
    publication = Field()  # 出版处
    publisher = Field()  # 出版方
    snippet = Field()  # 摘要片段
    keyword = Field()  # 关键词
    file_urls = Field()  # 下载链接
    # download_url = Field()
    search = Field()
    crawl_time = Field()