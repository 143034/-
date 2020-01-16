# -*- coding: utf-8 -*-
import scrapy
from paper_downloader.items  import PaperItem
from urllib import parse 
from copy import deepcopy  
import paper_downloader.key as Keyword
class HansSpider(scrapy.Spider):
    name = 'hans'
    allowed_domains = ['www.hanspub.org/']
    start_urls = ['https://www.hanspub.org/journal/Articles.aspx?searchCode=%s/'%(Keyword.get_search())]

    def parse(self, response):
        select = response.xpath('//*[@id="aritsear"]/div')
        for sele in select:
            url = sele.xpath('./div[2]/p[1]/a/@href').extract_first()
            url = parse.urljoin(response.url,url)
            yield scrapy.Request(url,callback=self.parse_detail,dont_filter=True)
            
        next_url = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_AspNetPager"]/a[text()="Next"]/@href').extract_first()
        next_url = parse.urljoin(response.url,next_url)
        if next_url is not None:
            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)
    def parse_detail(self, response):
        item = PaperItem()
        item['title'] = response.xpath('//*[@id="jouMain"]/div[1]/div[3]/ul/h1/b/text()').extract_first()
        author = response.xpath('//*[@id="jouMain"]/div[1]/div[3]/a/text()').extract()
        num = len(author)
        result = ''
        for i in range(num-1):
            result += author[i] + ','
        item['authors'] = result
        sel = response.xpath('//*[@id="ctl00_ContentPlaceHolder1_showJournalIssue"]/span/a/text()').extract_first()
        sel = sel.split('\r\n')[1].lstrip(' ')

        item['publicationDate'] = sel
        item['publication'] = 'Hans'
        item['publisher'] = 'Hans'
        item['snippet'] = response.xpath('//*[@id="jouMain"]/div[1]/div[3]/div[1]/div/p[1]/text()').extract_first()
        if item['snippet'] is None:
            item['snippet'] = response.xpath('//*[@id="jouMain"]/div[1]/div[3]/div[1]/div/div/span[1]/text()').extract_first() 
        sele = response.xpath('//*[@id="jouMain"]/div[1]/div[3]/p[2]/a/text()').extract()
        k = ''
        for j in range(len(sele)-2):
            k += sele[j] + ','
        item['keyword'] = k
        item['search'] = Keyword.get_search()


        url = response.xpath('//*[@id="clicknumber"]/@href').extract_first()
        url = parse.urljoin(response.url,url)
        yield scrapy.Request(url,callback=self.parse_download,meta={"item":deepcopy(item)},dont_filter=True)
    def parse_download(self, response):
        item = response.meta["item"]
        item['file_urls'] = [response.url]
        yield item


