#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/11 11:36
# software: PyCharm

from django.test.signals import setting_changed
from django.db.models.signals import pre_init

def f1(sender,**kwargs):
    print("xxoo")

pre_init.connect(f1)

# 自定义信号
# 创建一个信号 pizza = django.dispatch.Singal(providing_args=['',''])
# 注册一个信号 connect
# 触发一个信号 send
# 信号中注册函数


