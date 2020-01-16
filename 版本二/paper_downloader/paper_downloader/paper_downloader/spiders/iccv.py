# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items import PaperItem 
import paper_downloader.key as Keyword
class IccvSpider(scrapy.Spider):
    name = 'iccv'
    allowed_domains = ['openaccess.thecvf.com']
    start_urls = ['http://openaccess.thecvf.com/ICCV%s.py/'%(Keyword.get_search_three())]

    def parse(self, response):
        sele = response.xpath('//*[@id="content"]/dl/dt')
        for sel in sele:
            item = PaperItem()
            item['title'] = sel.xpath('./a/text()').extract_first()
            item['authors'] = sel.xpath('./following-sibling::dd/form/a/text()').extract()[0]
            item['file_urls'] =['http://openaccess.thecvf.com/' + sel.xpath('./following-sibling::dd/a/@href').extract_first()]
            # item['download_url'] ='http://openaccess.thecvf.com/' + sel.xpath('./following-sibling::dd/a/@href').extract_first()
            item['publicationDate'] = 'ICCV'
            item['publication'] = 'ICCV'
            item['publisher'] = 'ICCV'
            item['keyword'] = 'ICCV'
            item['search'] = 'ICCV'
            item['snippet'] = 'ICCV'
            yield item
