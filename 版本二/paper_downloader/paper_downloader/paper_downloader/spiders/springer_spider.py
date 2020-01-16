# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from paper_downloader.items import PaperItem
import paper_downloader.key as Keyword
# import time

class SpringerSpider(scrapy.Spider):
    name = 'springer_spider'
    allowed_domains = ['link.springer.com']
    start_urls = ['https://link.springer.com/']

    search = Keyword.get_search()
    # time.sleep(1)
    # start_search = get_search()
    # search = start_search
    start_url = 'https://link.springer.com/search?query={search}&showAll=false&facet-content-type="Article"'  # 第一页的url
    other_url = 'https://link.springer.com/search/page/{page}?showAll=false&query={search}&facet-content-type="Article"'  # 其他页码的url

    def start_requests(self):
        yield Request(self.start_url.format(search=self.search), self.parse_first)

    def parse_first(self, response):
        papers_list = response.xpath("//ol[@class='content-item-list']/li")
        for papers_item in papers_list:
            paper = PaperItem()
            paper['title'] = "".join(papers_item.xpath("./h2/a//text()").getall()).replace("\n", "").replace("  ", "")
            paper['snippet'] = (
                "".join(papers_item.xpath("./p[@class='snippet']/text()").getall()).replace("\n", "")).strip()
            paper['authors'] = ",".join(
                papers_item.xpath("./p[@class='meta']/span[@class='authors']/a/text()").getall())
            paper['publication'] = papers_item.xpath("./p[@class='meta']/span[@class='enumeration']/a/text()").get()
            paper['publicationDate'] = papers_item.xpath(
                "./p[@class='meta']/span[@class='enumeration']/span/@title").get()
            paper['publisher'] = 'Springer'
            paper['file_urls'] = ['https://link.springer.com' + papers_item.xpath(
                ".//span[@class='action'][1]/a/@href").get()]
            # paper['download_url'] = 'https://link.springer.com' + papers_item.xpath(
            #     ".//span[@class='action'][1]/a/@href").get()
            paper['search'] = self.search
            yield paper
        page_num = int("".join(
            response.xpath("//div[contains(@class,'functions-bar-top')]//span[@class='number-of-pages']/text()").get()))
        if page_num > 20:
            page_num = 20
        for page in range(2, page_num + 1):
            yield Request(self.other_url.format(page=page, search=self.search), callback=self.parse_other)

    def parse_other(self, response):
        papers_list = response.xpath("//ol[@class='content-item-list']/li")
        for papers_item in papers_list:
            paper = PaperItem()
            paper['title'] = "".join(papers_item.xpath("./h2/a//text()").getall()).replace("\n", "").replace("  ", "")
            paper['snippet'] = (
                "".join(papers_item.xpath("./p[@class='snippet']/text()").getall()).replace("\n", "")).strip()
            paper['authors'] = ",".join(
                papers_item.xpath("./p[@class='meta']/span[@class='authors']/a/text()").getall())
            paper['publication'] = papers_item.xpath("./p[@class='meta']/span[@class='enumeration']/a/text()").get()
            paper['publicationDate'] = papers_item.xpath(
                "./p[@class='meta']/span[@class='enumeration']/span/@title").get()
            paper['publisher'] = 'Springer'
            # paper['file_urls'] = ['https://link.springer.com' + papers_item.xpath(
            #     ".//span[@class='action'][1]/a/@href").get()]
            paper['search'] = self.search
            yield paper
