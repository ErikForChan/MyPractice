#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/2/28 13:03
# software: PyCharm

import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://www.autohome.com.cn/beijing/")
# reponse.encoding = 'UTF-8'
print(reponse.text)  # 文本
print(reponse.content)  # 原始字节

# soup = BeautifulSoup(reponse.text,"html.parser")
# tag = soup.find(id="auto-header-inner",class_='')
# h3 = tag.find(name='a')
# a_s = tag.find_all(name='a')
# for a in a_s:
#     print(a)
# print(h3.attrs)  # 字典，存储了多有属性
# class_content = h3.get('class') # 属性内容
