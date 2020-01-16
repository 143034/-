# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items import PaperItem 
from copy import deepcopy
import paper_downloader.key as Keyword
class CvprSpider(scrapy.Spider):
    name = 'cvpr'
    allowed_domains = ['openaccess.thecvf.com']
    start_urls = ['http://openaccess.thecvf.com/CVPR%s.py'%(Keyword.get_search_three())]
    def parse(self,response):
        sele = response.xpath('//*[@id="content"]/dl/dt')
        for sel in sele:
            item = PaperItem()
            item['title'] = sel.xpath('./a/text()').extract_first()
            item['file_urls'] =['http://openaccess.thecvf.com/' + sel.xpath('./following-sibling::dd/a/@href').extract_first()]
            item['publicationDate'] = 'CVPR'
            item['publication'] = 'CVPR'
            item['publisher'] = 'CVPR'
            item['keyword'] = 'CVPR'
            item['search'] = 'CVPR'
            # paper['snippet'] = 'CVPR'
            url = 'http://openaccess.thecvf.com/' + sel.xpath('./a/@href').extract_first()
            yield scrapy.Request(url,callback=self.parse_detail,meta={"item":deepcopy(item)})
    def parse_detail(self,response):
        item = response.meta["item"]
        item['authors'] = str(response.xpath('//*[@id="authors"]/b/i/text()').extract())
        item['snippet'] = str(response.xpath('//*[@id="abstract"]/text()').extract_first()).lstrip(' ').lstrip('\n')
        # item['publicationDate'] = response.xpath('//*[@id="authors"]/text()').extract()
        # paper['publicationDate'] = publicationDate[1].lstrip() + '-' + publicationDate[2][4:].lstrip(';').lstrip(' ').rstrip('\n')
        yield item


