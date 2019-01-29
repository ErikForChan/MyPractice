#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/25 17:02
# software: PyCharm

# yield把一个普通的函数变成了一个生成器
# def gen():
#     for i in range(10):
#         yield i*i
#
#
# fun = gen()
# for data in fun:
#     print(data)
# fun.__next__()

import time


def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield "return返回的值..."
       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

c = consumer("小华")
print('-------华丽分割线1-------------')
print(c.__next__())
print('-------华丽分割线2-------------')
print(c.__next__())
print('-------华丽分割线3-------------')
c.send("韭菜包")


# b1= "韭菜馅"
# c.send(b1)
# c.__next__()

# def producer(name):
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print("老子开始准备做包子啦!")
#     for i in range(10):
#         time.sleep(1)
#         print("做了1个包子,分两半!")
#         c.send(i)
#         c2.send(i)
#
# producer("alex")