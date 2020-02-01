# -*- coding: utf-8 -*-
import scrapy
from project.items import Pro_ProjectItem
import re
class ProPneumoniaSpider(scrapy.Spider):
    name = 'pro_pneumonia'
    allowed_domains = ['sa.sogou.com']
    start_urls = ['http://sa.sogou.com/new-weball/page/sgs/epidemic']

    def parse(self, response):
        start_data = response.body.decode()
        sele = re.findall('"provinceDetail":.*确诊 \d 例"]}',start_data)
        obj_list_start = sele[0].split(":")[1][1:-2].split(',')

        for i in obj_list_start:
            item = Pro_ProjectItem()
            s = i[1:-1].split(",")[0].split()
            s.pop()
            for j in range(0,(len(s)-1)):
                if s[j] == '例，疑似':
                    s.remove(s[j+1])
            if '例，疑似' in s:
                s.remove('例，疑似')


            num = len(s)
            item['province_Name'] = s[0]
            item['province_Confirmed'] = s[2]
            if num == 3:
                item['province_Death'] = 0
                item['province_Healing'] = 0
            elif num == 5:
                if s[3][2:] == "治愈":
                    item['province_Healing'] = s[4]
                    item['province_Death'] = 0
                else:
                    item['province_Healing'] = 0
                    item['province_Death'] = s[4]
            else:
                item['province_Healing'] = s[4]
                item['province_Death'] = s[6]
            yield item


