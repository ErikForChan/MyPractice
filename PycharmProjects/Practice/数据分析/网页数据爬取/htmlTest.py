#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 18:56
# software: PyCharm
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')

html = response.read()
soup = BeautifulSoup(html,"html.parser")

print(soup.find('a'))
