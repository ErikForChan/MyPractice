#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/18 18:37
# software: PyCharm

import matplotlib
from pandas import read_csv
import matplotlib.pyplot as plt

data = read_csv("data/data1.csv")
font = {
    'family':'SimHei'
}
matplotlib.rc('font',**font)

plt.hist(data['购买用户数'],bins=10)
plt.show()

