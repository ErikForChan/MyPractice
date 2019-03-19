#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/9 14:42
# software: PyCharm

from greenlet import greenlet


def fun1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def fun2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr2.switch()