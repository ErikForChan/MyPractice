#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/22 8:24
# software: PyCharm
import numpy
from pandas import read_csv
import pandas

data = read_csv("data/data3.csv")

bins = [min(data.年龄)-1, 20, 30, 40, max(data.年龄)+1];
labels = ['20岁以及以下', '21岁到30岁', '31岁到40岁', '41岁以上'];

年龄分层 = pandas.cut(data.年龄, bins, labels=labels)

data['年龄分层'] = 年龄分层;

r1=data.pivot_table(
    values=['年龄'],
    index=['年龄分层'],
    columns=['性别'],
    aggfunc=[numpy.size,numpy.mean]
)

r2=data.pivot_table(
    values=['年龄'],
    index=['年龄分层'],
    columns=['性别'],
    aggfunc=[numpy.std]
)

r = r1.join(r2)
print(r)

