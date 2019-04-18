#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 17:21
# software: PyCharm

import matplotlib
from pandas import read_csv
import matplotlib.pyplot as plt

data = read_csv("data/data1.csv")
font = {
    'family':'SimHei'
}
matplotlib.rc('font',**font)

plt.plot(data['广告费用'],data["购买用户数"],'.',color='red')

plt.xlabel('广告费用')
plt.ylabel("购买用户数")
plt.grid(True)

plt.show()

