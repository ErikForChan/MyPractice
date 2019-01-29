#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/4 17:22
# software: PyCharm

import importlib

mName = "lib.test"
module = importlib.import_module(mName)
module.getName()