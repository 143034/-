from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from paper_downloader.spiders.acm import AcmSpider
from paper_downloader.spiders.cnki import CnkiSpider
from paper_downloader.spiders.springer_spider import SpringerSpider
from paper_downloader.spiders.cvpr import CvprSpider
from paper_downloader.spiders.iccv import IccvSpider
from paper_downloader.spiders.eccv import EccvSpider
from paper_downloader.spiders.hans import HansSpider
from paper_downloader.spiders.ICLR import IclrSpider
from paper_downloader.spiders.ICML import IcmlSpider
from paper_downloader.spiders.IJCAI import IjcaiSpider
from paper_downloader.spiders.NIPS import NipsSpider
def Run_Spider(sele):
	setting = get_project_settings()
	p = CrawlerProcess(settings=setting)
	p.crawl(sele)
	p.start()

def Run_Process_ACM_Spider():
	p1 = Process(target=Run_Spider, args=(AcmSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_CNKI_Spider():
	p1 = Process(target=Run_Spider, args=(CnkiSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_SPRINGER_Spider():
	p1 = Process(target=Run_Spider, args=(SpringerSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_CVPR_Spider():
	p1 = Process(target=Run_Spider, args=(CvprSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_ICCV_Spider():
	p1 = Process(target=Run_Spider, args=(IccvSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_ECCV_Spider():
	p1 = Process(target=Run_Spider, args=(EccvSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_HANS_Spider():
	p1 = Process(target=Run_Spider, args=(HansSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_Iclr_Spider():
	p1 = Process(target=Run_Spider, args=(IclrSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_Icml_Spider():
	p1 = Process(target=Run_Spider, args=(IcmlSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_Ijcai_Spider():
	p1 = Process(target=Run_Spider, args=(IjcaiSpider,))
	p1.daemon = True
	p1.start()
def Run_Process_Nips_Spider():
	p1 = Process(target=Run_Spider, args=(NipsSpider,))
	p1.daemon = True
	p1.start()