from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from spiders.pneumonia import PneumoniaSpider
from spiders.pro_pneumonia import ProPneumoniaSpider

def Run_Spider(sele):
    setting = get_project_settings()
    p = CrawlerProcess(settings=setting)
    p.crawl(sele)
    p.start()

def Run_all():
    p1 = Process(target=Run_Spider, args=(PneumoniaSpider,))
    p2 = Process(target=Run_Spider, args=(ProPneumoniaSpider,))
    p1.daemon = True
    p2.daemon = True
    p1.start()
    p2.start()