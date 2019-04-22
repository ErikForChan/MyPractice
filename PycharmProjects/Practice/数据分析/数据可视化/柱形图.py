#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 18:00
# software: PyCharm
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy
import matplotlib

data = read_csv("data/data4.csv")
font = {
    'family':'SimHei'
}
matplotlib.rc('font',**font)

d1 = '手机品牌'
d2 = '通信品牌'
v = '月消费'
gb = data.groupby(
    by=[d1,d2]
)['月消费（元）'].agg({
    '月消费':'sum'
})

d1size = gb.index.levels[0].size
d2size = gb.index.levels[1].size
index = numpy.arange(d1size)
colors = ['r','g','b']
# plt.bar(index,gb['月消费'],1,color='G')
# plt.xticks(index+1/2,gb.index)
# plt.show()

bsum = index*0.0
for i in range(0,d2size):
    print(i)
    print(gb.index.labels[1])
    subgb = gb[v][gb.index.labels[1]==i]
    bar = plt.bar(index*d2size+i,subgb,color = colors[i])
    # bsum+=subgb

lIndex = numpy.arange(d1size)*d2size
plt.xticks(lIndex + 3/2,gb.index.levels[0])

plt.legend(gb.index.levels[1])
# plt.barh(index,gb['月消费'],1,color='G')
# plt.yticks(index+1/2,gb.index)
plt.show()