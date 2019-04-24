#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/24 11:27
# software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # for color later on 颜色

plt.scatter(X, Y, s=75, c=T, alpha=.5)  #s SIze c Color
plt.xlim(-1.5, 1.5)
# plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
# plt.yticks(())  # ignore yticks

plt.show()
