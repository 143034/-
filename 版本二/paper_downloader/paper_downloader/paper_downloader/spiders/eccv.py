# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items import PaperItem
import paper_downloader.key as Keyword
class EccvSpider(scrapy.Spider):
    name = 'eccv'
    allowed_domains = ['openaccess.thecvf.com']
    start_urls = ['http://openaccess.thecvf.com/ECCV%s.py/'%(Keyword.get_search_three())]

    def parse(self, response):
        sele = response.xpath('//*[@id="content"]/dl/dt')
        for sel in sele:
            item = PaperItem()
            item['title'] = sel.xpath('./a/text()').extract_first()
            item['authors'] = sel.xpath('./following-sibling::dd/form/a/text()').extract()[0]
            item['file_urls'] =['http://openaccess.thecvf.com/' + sel.xpath('./following-sibling::dd/a/@href').extract_first()]
            # item['download_url'] ='http://openaccess.thecvf.com/' + sel.xpath('./following-sibling::dd/a/@href').extract_first()
            item['publicationDate'] = 'ECCV'
            item['publication'] = 'ECCV'
            item['publisher'] = 'ECCV'
            item['keyword'] = 'ECCV'
            item['search'] = 'ECCV'
            item['snippet'] = 'ECCV'
            yield item
