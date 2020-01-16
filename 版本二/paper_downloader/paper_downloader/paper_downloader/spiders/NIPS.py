# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items import PaperItem
import paper_downloader.key as Keyword
class NipsSpider(scrapy.Spider):
    name = 'NIPS'
    allowed_domains = ['papers.nips.cc']
    start_urls = ['http://papers.nips.cc/book/advances-in-neural-information-processing-systems-%s'%(Keyword.get_search_nips())]

    def parse(self, response):
        url_list = response.xpath('/html/body/div[2]/div/ul/li')
        for i in url_list:
            url = 'http://papers.nips.cc' + i.xpath('./a[1]/@href').extract_first()
            print(url)
            yield scrapy.Request(url,callback=self.parse_detail,dont_filter=True)

    def parse_detail(self,response):
        item = PaperItem()
        item['title'] = response.xpath('/html/body/div[2]/div/h2/text()').extract_first()
        author = response.xpath('/html/body/div[2]/div/ul/li//text()').extract()
        s = ''
        for i in author:
            s = s + i + ','
        item['authors'] = s.rstrip(',')
        item['file_urls'] = ['http://papers.nips.cc' + response.xpath('/html/body/div[2]/div/a[1]/@href').extract_first()]
        item['publicationDate'] = 'NIPS'
        item['publication'] = 'NIPS'
        item['publisher'] = 'NIPS'
        item['snippet'] = 'NIPS'
        item['keyword'] = 'NIPS'
        item['search'] = 'NIPS'
        yield item








'''
http://papers.nips.cc/book/advances-in-neural-information-processing-systems-23-2010
http://papers.nips.cc/book/advances-in-neural-information-processing-systems-24-2011
http://papers.nips.cc/book/advances-in-neural-information-processing-systems-25-2012


2010 - 2019

/html/body/div[3]/div/ul
'''