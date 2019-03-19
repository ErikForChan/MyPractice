# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from jiandan.items import JiandanItem
class Jiandan1Spider(scrapy.Spider):
    name = 'jiandan1'
    allowed_domains = ['jiandan.net']
    url = "http://i.jandan.net/ooxx/page-"
    page = 1
    start_urls = [url + str(page) + '#comments']

    def parse(self, response):
        browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        browser.maximize_window()
        browser.get(response.url)
        browser.implicitly_wait(15)
        a_list = browser.find_elements_by_link_text("[查看原图]")
        for a in a_list:
            item = JiandanItem()
            print(a.get_attribute('href'))
            item['img_url'] = a.get_attribute('href')
            yield item
        if self.page < 10:
            self.page += 1
        yield scrapy.Request(self.url + str(self.page) + "#comments", self.parse)


