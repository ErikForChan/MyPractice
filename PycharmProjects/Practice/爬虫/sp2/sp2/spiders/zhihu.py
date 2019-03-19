# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    # 定制起始url函数,返回生成器
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,dont_filter=True,callback=self.parse1)

    def parse1(self, response):
        from scrapy.http.cookies import CookieJar
        cookie_jar = CookieJar()  # 对象
        cookie_jar.extract_cookies(response, response.request)

        for k,v in cookie_jar._cookies.items():
            for i,j in v.items():
                for m,n in j.items():
                    self.cook_dict[m] = n.value

        post_dict = {

        }

        yield Request(
            url="",
            method='POST',
            cookies=self.cookie_dict,
            body="",
        )


    # def parse(self, response):
    #     pass
