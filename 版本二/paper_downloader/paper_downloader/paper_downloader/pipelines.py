# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
from scrapy.pipelines.files import FilesPipeline
import pymysql
from pymysql import DataError
from scrapy.exceptions import DropItem
from os.path import basename, dirname, join
from urllib.parse import urlparse
import sys
sys.path.append('..')
import PATHS
path_date = PATHS.CONFIG_ALL_DIR + r'\data.csv'
# import xlwt
import csv
class PaperDownloaderPipeline(object):
    # 过滤掉不能下载的item
    def process_item(self, item, spider):
        if not item.get("file_urls"):
            raise DropItem("Duplicate item found:%s" % item)
        return item


class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        try:
            item['crawl_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            file = item['file_urls']
            item['file_urls'] = file[0]
            item['authors'] = item['authors'][:-1]
            data = dict(item)
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            update = ','.join(["{key}=%s".format(key=key) for key in data])
            sql = 'INSERT INTO %s (%s) VALUES (%s) ON DUPLICATE KEY UPDATE %s' % (item.table, keys, values, update)
            self.cursor.execute(sql, tuple(data.values()) * 2)
            self.db.commit()
        except DataError:
            raise DropItem("Duplicate item strange:%s" % item)
        return item

class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        return join(basename(dirname(path)), basename(path))
 
class CsvPipeline():
    def __init__(self):
        self.writer = csv.writer(open(path_date,'w+',newline='',encoding='utf-8'))
        # 设置标题
        self.writer.writerow(['title','author','file_urls'])
        
    def process_item(self, item, spider):
        row = [item['title'],item['authors'],item['file_urls'][0]]
        self.writer.writerow(row)
 
        return item