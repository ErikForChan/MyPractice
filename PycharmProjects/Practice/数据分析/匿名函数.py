#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/16 19:01
# software: PyCharm

#可变长参数*args
# def printLine(name,*args):
#     print(name+"---")
#     for arg in args:
#         print(arg)

#可变长KV形式的参数**kwargs
# def printLine(name,**kwargs):
#     print(name+"---")
#     for arg in kwargs:
#         print(arg+' is  '+kwargs[arg])
#
#
# printLine('Ja',sex='oo  ',age='91  ')


# 匿名函数
value = lambda a,b:a+b  #value是一个函数
print(value(1,2))
