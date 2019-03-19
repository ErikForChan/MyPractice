# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jiandan.net']
    start_urls = ['http://jiandan.net/']

    # 定制起始url函数,返回生成器
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse1)

    def parse1(self, response):
        hxs = Selector(response)
        text_list =  hxs.xpath('//div[@class="indexs"]/h2/a/text()').extract()
        # with open('jiandan.log','w') as f:
        #     for t in text_list:
        #         f.write(t)
        h_list = hxs.xpath('//div[@class="indexs"]/h2')
        for tag in h_list:
            url = tag.xpath('./a/@href')
            text = tag.xpath('./a/text()')
            from ..items import Sp2Item
            yield Sp2Item(url = url,text = text)


    # def parse(self, response):
    #     pass
