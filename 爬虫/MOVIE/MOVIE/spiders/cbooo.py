# -*- coding: utf-8 -*-
import scrapy
import requests
from pandas import read_csv
from bs4 import BeautifulSoup
from pandas import DataFrame
import matplotlib.pyplot as plt
import matplotlib
import numpy

class CboooSpider(scrapy.Spider):
    name = 'cbooo'
    allowed_domains = ['www.cbooo.cn']
    start_urls = ['http://www.cbooo.cn/year?year=2019']
    font = {
        'family': 'SimHei'
    }
    matplotlib.rc('font', **font)

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html,"html.parser")
        # tbody = soup.find(id="topdatatr")
        print('-------------------------------------------------------------')
        # print(tbody)

        table = soup.find(id = "tbContent")
        trs = table.find_all(name = "tr")
        movies = []
        types = []
        profits = []
        prices = []
        countaries = []
        now_profits = []
        profits_rating=[]
        all_profits=[]
        count_rating = []
        days = []
        for index,tr in enumerate(trs):
            if index > 0 and index <11:
                print(tr,end="\n")
                tds = tr.find_all(name = "td")
                for index2,td in enumerate(tds):
                    content = td.getText()
                    if index2 == 0:
                        pTag = td.find(name="p")
                        movies.append(pTag.getText())
                    elif index2 == 1:
                        # now_profits.append(float(content))
                        types.append(content)
                    elif index2 == 2:
                        # profits_rating.append(content)
                        profits.append(int(content))
                    elif index2 == 3:
                        # all_profits.append(float(content))
                        prices.append(int(content))
                    # elif index2 == 4:
                    #     count_rating.append(content)
                    #     profits_rating.append(content)
                    elif index2 == 5:
                        countaries.append(content)
                        # days.append(content)
        df = DataFrame({
            '影片名称': movies,
            '类型': types,
            '总票房': profits,
            '平均票价': prices,
            '国家/地区': countaries,
        })

        class1 = '影片名称'
        class2 = '国家/地区'
        gb_movie = df.groupby(
            by=[class1,class2]
        )['总票房'].agg({
            '总票房': 'sum'
        })
        # gb_country = df.groupby(
        #     by=[class2]
        # )['总票房'].agg({
        #     '总票房': 'sum'
        # })
        # print(gb)
        # print(gb,index)
        # size1 = gb.index.levels[0].size
        # size2 =  gb.index.levels[1].size
        # index1 = numpy.arange(size1)
        # colors = ['r', 'g']
        print('-------------------------------------------------------------')
        # for i in range(0, size2):
        #     print(gb.index.labels[1])
        #     subgb = gb["总票房"][gb.index.labels[1] == i]
        #     plt.bar(index1 * size2 + i, subgb, color=colors[i])
        # plt.barh(range(len(profits)), profits, tick_label=movies,color='rgb')
        # plt.bar(df['影片名称'], df['实时票房'], 1, color='G')
        # # plt.plot(df['影片名称'],df['实时票房'],  '-',color='red')

        # plt.bar(index1 * size2 , subgb, color=colors[i])
        # lIndex = numpy.arange(size1) * size2
        # plt.xticks(lIndex + 3 / 2, gb.index.levels[0])
        # print(gb_movie["总票房"])
        # plt.bar(range(gb_movie.index.levels[0].size), profits,tick_label =  movies)
        # bet = numpy.arange(gb_movie.index.levels[0].size)
        # plt.xticks(bet,gb_movie.index.levels[0])
        # print(gb_movie["总票房"][gb_movie.index.labels[1] == 1])
        print(gb_movie.index.labels)
        plt.barh(range(len(profits)), profits, tick_label=movies,color='rgb')

        # plt.pie(df['总票房'], labels=df['影片名称'],autopct='%.2f%%')
        plt.title("票房统计图")
        # plt.grid(True)
        # plt.legend(gb.index.levels[1])
        plt.show()


