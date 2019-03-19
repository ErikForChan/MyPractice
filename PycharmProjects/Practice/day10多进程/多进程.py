#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/10 14:57
# software: PyCharm

import multiprocessing
import time


def run(n):
    print("进程%s"% str(n))
    time.sleep(1)


if __name__ == "__main__":

    for i in range(10):
        p = multiprocessing.Process(target=run,args=(i,)) #创建多进程和
        p.start() #启动多进程