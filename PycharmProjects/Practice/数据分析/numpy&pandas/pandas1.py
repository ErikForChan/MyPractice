#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/22 15:46
# software: PyCharm

import pandas as pd
import numpy as np

# s = pd.Series([1,2,3,4,5,6])
# dates = pd.date_range(20160101,periods=6)
# df = pd.DataFrame(
#     np.random.randn(6,4),
#     index=dates,
#     columns=['a','b','c','d']
# )
#
# df.sort_index(axis=1,ascending=False) #列倒叙排列
#
# #数据选择
# df.loc['20130102']
# df.loc[:,['a','b']]
# df.iloc[3:5,1:3]
# df.ix[3,['a']]
# df[df.a > 3]
#
# #设置值
# df.b[df.a > 5] = 0
#
# #处理丢失数据
# df.dropna(axis=0,how='any') #how='all'
# df.fillna(value=0)
# df.isnull() #返回一个df，每个数据为True或False
#
# #合并concat
# df1 = pd.DataFrame(
#     np.random.randn(6,4),
#     index=dates,
#     columns=['a','b','c','d']
# )
# pd.concat([df,df1],axis=0,ignore_index=True)
# r1 = pd.concat([df,df1],join='outer') #join='innner'
# pd.concat([df,df1],join_axes=[df.index])
# df.append(df1,ignore_index=True)

#合并merge
# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                              'key2': ['K0', 'K1', 'K0', 'K1'],
#                              'A': ['A0', 'A1', 'A2', 'A3'],
#                              'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                               'key2': ['K0', 'K0', 'K0', 'K0'],
#                               'C': ['C0', 'C1', 'C2', 'C3'],
#                               'D': ['D0', 'D1', 'D2', 'D3']})
# res = pd.merge(left,right,on=['key1','key2'],how='inner',indicator="合并方式",suffixes=['qq1','qq2']) #indicator 显示合并方式
# print(res)

import matplotlib.pyplot as plt
import matplotlib
font = {
    'family':'SimHei'
}
matplotlib.rc('font',**font)

data = pd.Series(
    np.random.randn(1000),
    index=np.arange(1000),
)
data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list('ABCD')
)
data = data.cumsum()
# print(data)
# data.cumsum()
# data.plot.scatter(x='A',y='B',color = 'Blue',label = "c1")
data.plot()


plt.xlabel('广告费用')
plt.ylabel("购买用户数")
plt.show()



