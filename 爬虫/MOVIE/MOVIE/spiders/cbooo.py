# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import pandas as pd

class CboooSpider(scrapy.Spider):
    name = 'cbooo'
    allowed_domains = ['www.cbooo.cn']
    start_urls = ['http://www.cbooo.cn/']

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html,"html.parser")
        tbody = soup.find(id="topdatatr")
        print('-------------------------------------------------------------')
        # print(tbody)
        trs = tbody.find_all(name = "tr")
        for tr in trs:
            tds = tr.find_all(name = "td")
            for td in tds:
                print(td.getText())
        print('-------------------------------------------------------------')
