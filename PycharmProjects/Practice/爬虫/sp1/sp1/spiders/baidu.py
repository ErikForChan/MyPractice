# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http import Request


class BaiduSpider(scrapy.Spider):
    name = 'xiaohuar1'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']

    def parse(self, response):
        # hxs = HtmlXPathSelector(response)
        # //子孙目录找 /儿子目录中找 .相对于当前位置找 ./当前的子孙目录找 ''子目录中找
        hxs = Selector(response = response)
        # user_list = hxs.xpath('//div[@class="item masonry_brick"]')
        # print("Test: ")
        # print(user_list)
        # for user in user_list:
        #     price = user.xpath('./span[@class="price"]/text()').extract_first()
        #     url = user.xpath('div[@class="item_t"]/div[@class="class"]//a/@href').extract_first()
        #     print(price, url)

        result = hxs.xpath('/a[re:test(@href,"http://www.xiaohuar.com/list-1-\d+.html")]/@href')
        print(result)

        # 循环url列表，发请求
        for url in result:
            yield Request(url = url,callback=self.parse)
