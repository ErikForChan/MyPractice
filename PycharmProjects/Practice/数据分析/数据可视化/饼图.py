#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 17:50
# software: PyCharm
import matplotlib
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy

data = read_csv("data/data3.csv")
font = {
    'family':'SimHei'
}
matplotlib.rc('font',**font)

gb = data.groupby(
    by=['通信品牌'],
    as_index=False
)['号码'].agg({
    '用户数':numpy.size
})

plt.pie(gb['用户数'],labels=gb['通信品牌'],autopct='%.2f%%')
plt.show()

