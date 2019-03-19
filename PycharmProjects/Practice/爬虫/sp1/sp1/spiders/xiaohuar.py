# -*- coding: utf-8 -*-
import scrapy


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']

    def parse(self, response):
        # 获取制定数据，进行持久化

        # 获取
        pass
