# -*- coding: utf-8 -*-
import scrapy,sys
# print(sys.path)
# sys.path.append('..')
# print(sys.path)
from project.items import ProjectItem
# from project.items import ProjectItem
import re
import time
class PneumoniaSpider(scrapy.Spider):
    name = 'pneumonia'
    allowed_domains = ['sa.sogou.com']
    start_urls = ['http://sa.sogou.com/new-weball/page/sgs/epidemic']

    def parse(self, response):
        item = ProjectItem()
        sele = response.body.decode()
        time_update = int(re.findall('"timestamp":\d+',sele)[0].split(':')[1][:-3])
        time_result = time.localtime(time_update)
        StyleTime = time.strftime("%Y--%m--%d %H:%M:%S", time_result)
        item['Confirmed'] = re.findall('"diagnosed":\d+',sele)[0].split(':')[1]
        item['Suspected'] = re.findall('"suspect":\d+',sele)[0].split(':')[1]
        item['Healing'] = re.findall('"cured":\d+', sele)[0].split(':')[1]
        item['Death'] = re.findall('"death":\d+',sele)[0].split(':')[1]
        item['Deadline'] = StyleTime
        yield item
'''




'''