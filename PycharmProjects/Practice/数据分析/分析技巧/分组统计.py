#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/19 19:52
# software: PyCharm
import numpy
from pandas import read_csv

data = read_csv("data/data2.csv")

gb = data.groupby(
    by=['class','name']
)['score'].agg(
    {
        '总分':numpy.sum
    }
)

print(gb)
