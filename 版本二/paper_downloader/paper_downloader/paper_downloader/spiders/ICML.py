# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items import PaperItem
import paper_downloader.key as Keyword
class IcmlSpider(scrapy.Spider):
    name = 'ICML'
    allowed_domains = ['proceedings.mlr.press']
    start_urls = ['http://proceedings.mlr.press/%s/'%(Keyword.get_search_icml())]

    def parse(self, response):
        obj_list = response.xpath('//*[@id="content"]/div/div')[1:]
        for obj in obj_list:
            item = PaperItem()
            item['title'] = obj.xpath('./p[1]/text()').extract_first()
            item['file_urls'] = [obj.xpath('./p[3]/a[2]/@href').extract_first()]
            author = obj.xpath('./p[2]/span/text()').extract_first()
            aut_list = author.split(",")
            s = ''
            for i in aut_list:
                s = s + i.lstrip('\n').lstrip(' \n\n      \n      ').rstrip('\n\n      \n    ') + ','

            item['authors'] = s[:-1]
            item['publicationDate'] = 'ICML'
            item['publication'] = 'ICML'
            item['publisher'] = 'ICML'
            item['snippet'] = 'ICML'
            item['keyword'] = 'ICML'
            item['search'] = 'ICML'
            yield item
'''
https://link.springer.com/search?facet-journal-id=11263&package=openaccessarticles&search-within=Journal&query=&date-facet-mode=in&facet-start-year=2017&previous-start-year=2008&facet-end-year=2017&previous-end-year=2018
//*[@id="content"]/div/div[2]/p[3]/a[2]

v97 --- 2019
v70  --- 2017



//*[@id="content"]/div/div[2]/p[2]/span[1]
'''