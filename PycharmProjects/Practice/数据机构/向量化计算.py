#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/16 19:13
# software: PyCharm

import numpy

#生成一个等差数列
r = numpy.arange(0.1,7)

# 四则运算
count = r+1
print(count)
#次方
rc = numpy.power(r,5)
print(rc)
#矩阵运算
jz = numpy.dot(r,r.T)
print(jz)