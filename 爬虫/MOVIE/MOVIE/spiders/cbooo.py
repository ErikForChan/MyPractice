# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib
import numpy

class CboooSpider(scrapy.Spider):
    name = 'cbooo'
    allowed_domains = ['www.cbooo.cn']
    start_urls = ['http://www.cbooo.cn/']
    font = {
        'family': 'SimHei'
    }
    matplotlib.rc('font', **font)

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html,"html.parser")
        tbody = soup.find(id="topdatatr")
        print('-------------------------------------------------------------')
        # print(tbody)
        trs = tbody.find_all(name = "tr")
        movies = []
        now_profits = []
        profits_rating=[]
        all_profits=[]
        count_rating = []
        days = []
        for tr in trs:
            tds = tr.find_all(name = "td")
            for index,td in enumerate(tds):
                content = td.getText()
                if index == 1:
                    movies.append(content)
                elif index == 2:
                    now_profits.append(content)
                elif index == 3:
                    profits_rating.append(content)
                elif index == 4:
                    all_profits.append(content)
                elif index == 5:
                    count_rating.append(content)
                elif index == 6:
                    days.append(content)
        df = DataFrame({
            '影片名称': movies,
            '实时票房': now_profits,
            '票房占比': profits_rating,
            '累计票房': all_profits,
            '排片占比': count_rating,
            '上映天数': days,
        })
        print(df)
        print('-------------------------------------------------------------')
        # gb = df.groupby(
        #     by=['影片名称'],
        #     as_index=False
        # )['实时票房'].agg({
        #     '用户数': numpy.size
        # })

        plt.plot(df['影片名称'],df['实时票房'],  '-',color='red')
        # plt.pie(df['实时票房'], labels=df['影片名称'])
        plt.show()


