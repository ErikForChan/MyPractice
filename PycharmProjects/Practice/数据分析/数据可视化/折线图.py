#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 17:42
# software: PyCharm
import matplotlib
from pandas import read_csv
import matplotlib.pyplot as plt
data = read_csv("data/data2.csv")
font = {
    'family':'SimHei'
}
matplotlib.rc('font',**font)

plt.plot(data['日期'],data['购买用户数'],'-',color='blue')
# plt.xlabel('日期')
# plt.ylabel("购买用户数")
plt.grid(True)
plt.title("购买用户数时间序列图")
plt.show()
