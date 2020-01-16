# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items import PaperItem
import paper_downloader.key as Keyword
class IjcaiSpider(scrapy.Spider):
    name = 'IJCAI'
    allowed_domains = ['www.ijcai.org/']
    start_urls = ['http://www.ijcai.org/proceedings/%s/'%(Keyword.get_search_three())]

    def parse(self, response):
        obj_list = response.xpath('//*[@class="section"]')[1:]
        for obj in obj_list:
            sele = obj.xpath('./div[2]/div')
            for sel in sele:
                item = PaperItem()
                item['title'] = sel.xpath('./div[1]/text()').extract_first()
                item['authors'] = sel.xpath('./div[2]/text()').extract_first()
                URL = sel.xpath('./div[3]/a[1]/@href').extract_first()
                if URL is not None:
                    item['file_urls'] = ['http://www.ijcai.org/proceedings/%s/'%(Keyword.get_search_three()) + URL]
                item['publicationDate'] = 'IJCAI'
                item['publication'] = 'IJCAI'
                item['publisher'] = 'IJCAI'
                item['snippet'] = 'IJCAI'
                item['keyword'] = 'IJCAI'
                item['search'] = 'IJCAI'
                yield item






    '''
    
    2017-2018
    

    '''
