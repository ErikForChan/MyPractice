#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/22 8:36
# software: PyCharm

import numpy
from pandas import read_csv
import pandas

data = read_csv("data/data5.csv")

data_pt = data.pivot_table(
    values=['月消费（元）'],
    index=['省份'],
    columns=['通信品牌'],
    aggfunc=[numpy.sum]
)

data_pt.sum(axis = 0) #按列运算
data_pt.sum(axis = 1) #按行运算


