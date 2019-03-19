#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2018/12/27 17:01
# software: PyCharm

import random
checkcode = ''
for i in range(4):
    data = random.randrange(0,5)
    if(data == i):
        temp = chr(random.randrange(65,90))
    else:
        temp = random.randint(0,9)

    checkcode += str(temp)

print(checkcode)