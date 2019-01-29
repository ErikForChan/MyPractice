#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/4 18:46
# software: PyCharm

mName = "lib.test"

module = __import__(mName,fromlist = ('test',))
module.getName()