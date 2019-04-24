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

# plt.figure()
# plt.plot(x,y2)

#设置坐标轴范围
plt.xlim((-1,2))
plt.ylim((-2,3))

#设置坐标轴名称
plt.xlabel("I'm X")
plt.ylabel("I'm Y")

#坐标轴数字
# new_ticks = np.linspace(-1.2,5);
# plt.xticks(new_ticks)
# plt.xticks(new_ticks,['用名称代替数字'])

ax= plt.gca()
ax.spines['right'].set_color('none') #右边实线消失
ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('buttom')
# ax.yaxis.set_ticks_position('left')

#原点设在哪个位置
# ax.spines['buttom'].set_position('data',0)
# ax.spines['left'].set_position('data',0)

l1, = plt.plot(x,y2,color = 'red',linestyle='-',linewidth=3,label='down')
l2, = plt.plot(x,y1,color = 'green',linestyle='--',linewidth=1,label='up')
#Legend图例
plt.legend(loc='best',handles=[l1,l2,]) #添加两个图例

plt.show()

