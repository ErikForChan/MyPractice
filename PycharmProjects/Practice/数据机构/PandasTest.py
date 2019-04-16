#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/16 18:46
# software: PyCharm
from pandas import Series

x = Series(['a',True,1],index=['f','s','t'])
# print(x['s'])
# n = Series(['2'])
# x.append(n)
# print(x[0])
#
# #删除
# x.drop(0)  # x.drop('f')


from pandas import DataFrame

df = DataFrame({
    'age':[11,33,66],
    'name':['Jack','Mark','John']
},index=['f','s','t']);

print(df['age'])


