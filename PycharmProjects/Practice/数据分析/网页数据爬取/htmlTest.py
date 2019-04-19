#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 18:56
# software: PyCharm
from bs4 import BeautifulSoup
import urllib.request
from pandas import DataFrame,Series
response = urllib.request.urlopen('http://www.metvb.info/')

html = response.read()
soup = BeautifulSoup(html,"html.parser")

mbs= soup.find_all(class_='mb')
data = DataFrame(columns=['电影名称','网址'])
for mb in mbs:
    name = mb.find("p",class_='name')
    imgsrc = mb.find("img",class_="lazy")['data-original']
    # img = mb.find("img",class_="lazy")
    # print(name.getText())
    # print(img)
    # print(imgsrc)
    data = data.append(
           Series(
               [name.getText(),imgsrc],index=['电影名称','网址']
           ),ignore_index=True
    )

print(data)