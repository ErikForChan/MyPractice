# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup

from selenium import webdriver

class MetvbSpider(scrapy.Spider):
    name = 'metvb'
    allowed_domains = ['www.metvb.info']
    start_urls = ['http://www.metvb.info/']

    def parse(self, response):
        html = response.text
        # browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        # browser.maximize_window()
        # browser.get(response.url)
        # browser.implicitly_wait(15)
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        lis = soup.find_all(class_='mb')
        for li in lis:
            img = li.find(name="img")
            print(img.getattr("data-original"))
        # print(lis)
