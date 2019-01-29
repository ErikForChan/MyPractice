#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/9 14:53
# software: PyCharm

import gevent


def foo():
    print('foo1')
    gevent.sleep(2)
    print('foo2')
    gevent.sleep(1)


def bar():
    print('bar1')
    gevent.sleep(1)


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
])

