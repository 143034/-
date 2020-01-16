# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request
from paper_downloader.items  import PaperItem
import re
# from paper_downloader.keywords import get_search
# import time
import paper_downloader.key as Keyword

class AcmSpider(scrapy.Spider):
    name = 'acm'
    allowed_domains = ['dl.acm.org']
    start_urls = ['https://dl.acm.org/']
    search = Keyword.get_search()
    # time.sleep(1)
    # start_search = get_search()
    # search = start_search
    start_url = 'https://dl.acm.org/results.cfm?query={search}&Go.x=0&Go.y=0'  # 第一页的url
    other_url = 'https://dl.acm.org/results.cfm?query={search}&start={start}&filtered=&within=owners%2Eowner%3DHOSTED&dte=&bfr=&srt=_score'  # 其他页码的url

    def start_requests(self):
        yield Request(self.start_url.format(search=self.search), self.parse_first)

    def parse_first(self, response):
        papers_list = response.xpath("//div[@class='details']")
        for papers_item in papers_list:
            paper = PaperItem()
            if 'title' in str(papers_item.xpath("./div/@class")):
                paper['title'] = papers_item.xpath("./div[@class='title']/a/text()").extract_first()
            if 'authors' in str(papers_item.xpath("./div/@class")):
                paper['authors'] = ','.join(papers_item.xpath("./div[@class='authors']/a/text()").extract())
            if 'source' in str(papers_item.xpath("./div/@class")):
                paper['publicationDate'] = papers_item.xpath("///span[@class='publicationDate']/text()").extract_first()
                paper['publication'] = papers_item.xpath("./div[@class='source']/span[2]/text()").extract_first()
            if 'publisher' in str(papers_item.xpath("./div/@class")):
                paper['publisher'] = papers_item.xpath("./div[@class='publisher']/text()").extract()[1].replace("\xa0",
                                                                                                                "").replace(
                    "\n", "")
            if 'ft' in str(papers_item.xpath("./div/@class")):
                paper['file_urls'] = ['https://dl.acm.org/' + papers_item.xpath(
                    "./div[@class='ft']/a/@href").extract_first()]
                # paper['download_url'] = 'https://dl.acm.org/' + papers_item.xpath(
                #     "./div[@class='ft']/a/@href").extract_first()
            if 'abstract' in str(papers_item.xpath("./div/@class")):
                paper['snippet'] = papers_item.xpath("./div[@class='abstract']/text()").extract_first().replace("\n",
                                                                                                                "")
            if 'kw' in str(papers_item.xpath("./div/@class")):
                paper['keyword'] = papers_item.xpath("./div[@class='kw']/text()").extract()[1].strip(':').replace("\n",
                                                                                                                  "")
            paper['search'] = self.search
            yield paper
        start_num = int(
            re.compile(".*start=(\d*)").findall(str(response.xpath("//div[@class='pagelogic'][1]/a/@href")))[0])
        if start_num / 20 > 20:
            start_num = 400
        for start in range(20, start_num, 20):
            yield Request(url=self.other_url.format(search=self.search, start=start), callback=self.parse_other)

    def parse_other(self, response):
        papers_list = response.xpath("//div[@class='details']")
        for papers_item in papers_list:
            paper = PaperItem()
            if 'title' in str(papers_item.xpath("./div/@class")):
                paper['title'] = papers_item.xpath("./div[@class='title']/a/text()").extract_first()
            if 'authors' in str(papers_item.xpath("./div/@class")):
                paper['authors'] = ','.join(papers_item.xpath("./div[@class='authors']/a/text()").extract())
            if 'source' in str(papers_item.xpath("./div/@class")):
                paper['publicationDate'] = papers_item.xpath("///span[@class='publicationDate']/text()").extract_first()
                paper['publication'] = papers_item.xpath("./div[@class='source']/span[2]/text()").extract_first()
            if 'publisher' in str(papers_item.xpath("./div/@class")):
                paper['publisher'] = papers_item.xpath("./div[@class='publisher']/text()").extract()[1].replace("\xa0",
                                                                                                                "").replace(
                    "\n", "")
            if 'ft' in str(papers_item.xpath("./div/@class")):
                paper['file_urls'] = ['https://dl.acm.org/' + papers_item.xpath(
                    "./div[@class='ft']/a/@href").extract_first()]
                # paper['download_url'] = 'https://dl.acm.org/' + papers_item.xpath(
                #     "./div[@class='ft']/a/@href").extract_first()
            if 'abstract' in str(papers_item.xpath("./div/@class")):
                paper['snippet'] = papers_item.xpath("./div[@class='abstract']/text()").extract_first().replace("\n",
                                                                                                                "")
            if 'kw' in str(papers_item.xpath("./div/@class")):
                paper['keyword'] = papers_item.xpath("./div[@class='kw']/text()").extract()[1].strip(':').replace("\n",
                                                                                                                  "")
            paper['search'] = self.search
            yield paper
