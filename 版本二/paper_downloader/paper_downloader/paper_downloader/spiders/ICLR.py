# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from time import sleep
from paper_downloader.items import PaperItem


class IclrSpider(scrapy.Spider):
    name = 'ICLR'
    allowed_domains = ['openreview.net/']
    start_urls = ['https://www.baidu.com']

    def parse(self, response):

        yield scrapy.Request('https://www.baidu.com',callback=self.parse_detail,dont_filter=True)


    def parse_detail(self,response):

        url = 'https://openreview.net/group?id=ICLR.cc/2018/Conference#accepted-oral-papers'
        pjs_obj = webdriver.PhantomJS(
            executable_path=r'D://phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        pjs_obj.get(url)
        sleep(5)
        sele = pjs_obj.find_elements_by_xpath('//*[@id="accepted-oral-papers"]/ul/li')
        print(sele)
        for i in sele:
            item = PaperItem()
            item['title'] = i.find_element_by_xpath('./h4/a[1]').text
            item['file_urls'] = [i.find_element_by_xpath('./h4/a[2]').get_attribute('href')]
            item['authors'] = i.find_element_by_xpath('./div[1]').text
            item['publicationDate'] = 'ICLR'
            item['publication'] = 'ICLR'
            item['publisher'] = 'ICLR'
            item['snippet'] = 'ICLR'
            item['keyword'] = 'ICLR'
            item['search'] = 'ICLR'

            yield item
        yield scrapy.Request('https://www.baidu.com', callback=self.parse_detail_1, dont_filter=True)
    def parse_detail_1(self,response):
        pjs_obj = webdriver.PhantomJS(
            executable_path=r'D://phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        pjs_obj.get('https://openreview.net/group?id=ICLR.cc/2018/Conference#accepted-poster-papers')
        sleep(5)
        sele = pjs_obj.find_elements_by_xpath('//*[@id="accepted-poster-papers"]/ul/li')
        if sele is not None:
            for i in sele:
                item = PaperItem()
                item['title'] = i.find_element_by_xpath('./h4/a[1]').text
                item['file_urls'] = [i.find_element_by_xpath('./h4/a[2]').get_attribute('href')]
                item['authors'] = i.find_element_by_xpath('./div[1]').text
                item['publicationDate'] = 'ICLR'
                item['publication'] = 'ICLR'
                item['publisher'] = 'ICLR'
                item['snippet'] = 'ICLR'
                item['keyword'] = 'ICLR'
                item['search'] = 'ICLR'
'''
2014-2020
//*[@id="accepted-oral-papers"]/ul/li[1]/div[1]

2013,2014,2016,2017,2018,2019,2020
'''