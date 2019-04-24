#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/24 11:32
# software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(12)
Y1 = (1-X/float(12)) * np.random.uniform(0.5,1,12)
Y2 = (1-X/float(12)) * np.random.uniform(0.5,1,12)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-.5, 12)
# plt.xticks(())
plt.ylim(-1.25, 1.25)
# plt.yticks(())

plt.show()

