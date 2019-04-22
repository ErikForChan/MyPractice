#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/22 8:46
# software: PyCharm

import numpy
from pandas import read_csv
import pandas

data = read_csv("data/data6.csv")

r1 = data['人口'].corr(data['文盲率'])
print(r1)


#多列之间相关度
r2 = data.loc[:,['超市购物率', '网上购物率', '文盲率', '人口']].corr()
print(r2)