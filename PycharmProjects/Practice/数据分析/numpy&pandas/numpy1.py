#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/22 9:07
# software: PyCharm
import numpy as np

arr = ([
    [1,2,3],
    [2,3,4]
])
array = np.array(arr,dtype=int) #矩阵
print(array)
print(array.ndim) #几维数组
print(array.shape) #有多少行、多少列
print(array.size)

a = np.zeros((3,4)) #3行4列的全部为0的数
a = np.arange(10.20,2) #10到20之前的差为2 的等差数列
a.reshape(3,4)

a1 = np.linspace(1,20,5) #自动在1至20之间生成等差数列，一共5个数



# 四则运算
b = np.array([1,2,3,4])
b1 = np.arange(4)

b+b1
b-b1
b*b1
b**b1
np.sin(b)

b<3 #输出那些小于3 [True,False,True,True]

#矩阵的运算
c_dot = np.dot(b,b1)
b.dot(b1) #乘法

#随机的array
c1 = np.random.random((2,4))

np.sum(c1,axis=1)
np.max(c1)
c1,max()
np.argmax() #最大值的索引

#平均值
np.mean(c1)
c1.mean()
np.average(c1)

#中位数
np.median(c1)

#每两个数累加的结果
np.cumsum()
np.diff()

#非0
np.nonzero(a)

#排序
d = np.arange(10,2,-1)
np.sort(a)

#反向
np.transpose(a)
a.T


np.clip(a,3,6) #所有小于6的都变成6，小于3的都变成3

#将矩阵所有元素放在一个数组中
a.flatten()
for item in a.flat:
    print(item)

#合并
np.vstack((a,b))
a= [1,1,1]
a[:,np.newaxis] #换成竖的维度
C = np.concatenate((a,b,a)) #多个矩阵合并

#分割
a = np.arange(12).reshape((3,4))
np.split(a,2,axis=1)
np.vsplit(a,2)

#copy和deepcopy
e = a.copy() #只是把值复制，并没有互相关联


