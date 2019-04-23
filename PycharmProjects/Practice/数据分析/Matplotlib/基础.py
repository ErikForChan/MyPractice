#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/23 17:34
# software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x+1
y2 = x**2

plt.figure() #不同的figure放置不同的图
plt.plot(x,y1,color = 'red',linestyle='--',linewidth=3)

plt.figure()
plt.plot(x,y2)

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel("I'm X")
plt.ylabel("I'm Y")
plt.show()

