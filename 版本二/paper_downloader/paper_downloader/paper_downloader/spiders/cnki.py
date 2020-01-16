# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
from paper_downloader.items import PaperItem
import paper_downloader.key as Keyword
# import time
# path = str(os.path.split(os.path.realpath(__file__))[0]) + '\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=path)
class CnkiSpider(scrapy.Spider):
    name = 'cnki'
    allowed_domains = ['www.cnki.net']
    start_urls = ['http://www.cnki.net']
    search = Keyword.get_search()
    # time.sleep(1)
    # start_search = get_search()

    # search = start_search

    def parse(self, response):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        path = str(os.path.split(os.path.realpath(__file__))[0]) + '\chromedriver.exe'

        browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=path)
        try:
            browser.get(response.request.url)
            input = browser.find_element_by_id('txt_SearchText')
            input.send_keys(self.search)
            input.send_keys(Keys.ENTER)
            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'newsh_mid')))
            browser.switch_to.frame('iframeResult')
            browser.maximize_window()
            i = 10  # 取结果的前10页
            while i > 0:
                try:
                    i -= 1
                    print(i)
                    papers_list = browser.find_elements_by_xpath("//table[@class='GridTableContent']/tbody/tr")
                    for papers_item in papers_list[1:]:
                        paper = PaperItem()
                        paper['title'] = papers_item.find_element_by_class_name('fz14').text
                        authors = papers_item.find_elements_by_class_name('KnowledgeNetLink')
                        author = []
                        for au in authors:
                            author.append(au.text)
                        paper['authors'] = ','.join(author)
                        paper['publicationDate'] = papers_item.find_elements_by_tag_name('td')[4].text
                        paper['publication'] = papers_item.find_elements_by_tag_name('td')[3].text
                        paper['publisher'] = 'CNKI'
                        paper['snippet'] = None
                        paper['keyword'] = None
                        try:
                            download_url = papers_item.find_elements_by_tag_name("td")[7].find_element_by_tag_name(
                                'a').get_attribute('href')
                            paper['file_urls'] = [urljoin(response.request.url, download_url)]
                            # paper['download_url'] = urljoin(response.request.url, download_url)
                        except:
                            continue
                        a = 0
                        paper['search'] = self.search
                        yield paper
                    page = browser.find_element_by_partial_link_text('下一页')
                    # print(page.text)
                    browser.execute_script("arguments[0].scrollIntoView(false);", page)
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '下一页'))).click()
                except:
                    break
        finally:
            browser.close()
