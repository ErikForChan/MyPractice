#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/26 18:39
# software: PyCharm
# from collections import Iterable, Iterator


# 生成器
def func():
	for i in range(10):
            yield i


f = func()
# 遍历生成器
for i in f:
    print(i)
print(f.__next__())


# 迭代器可以存放无限个数据
# 判断列表是否可迭代
# list = [1,2,3,4,5,6]
# isinstance(list,Iterable)
# # 判断是否为一个迭代器
# iterMachine = (x for x in range(10))
# isinstance(iterMachine,Iterator)
#
# # 将列表转化为迭代器
# it = iter(list)
# print(it.__next__())
# print(next(it))

