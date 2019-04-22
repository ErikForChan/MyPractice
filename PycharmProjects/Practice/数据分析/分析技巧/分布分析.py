#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/20 14:40
# software: PyCharm

import numpy
from pandas import read_csv
import pandas
data = read_csv("data/data3.csv")


bins = [min(data.年龄)-1,20,30,40,max(data.年龄)-1]

labels = ['20岁以及以下', '21岁到30岁', '31岁到40岁', '41岁以上'];

年龄分层 = pandas.cut(data.年龄, bins, labels=labels)

data['年龄分层'] = 年龄分层;

data.groupby(by=['年龄分层'])['年龄'].agg({'人数':numpy.size})




