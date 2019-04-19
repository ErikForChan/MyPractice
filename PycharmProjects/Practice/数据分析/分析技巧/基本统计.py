#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/19 19:45
# software: PyCharm
from pandas import read_csv
import matplotlib.pyplot as plt

data = read_csv("data/data1.csv")
# print(data.score.describe())
print(data.score.size)
print(data.score.max())
print(data.score.min())
print(data.score.sum())
print(data.score.var())#方值
print(data.score.std()) #标准差
print(data.score.mean()) #平均值


