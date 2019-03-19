#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/8 9:33
# software: PyCharm
import threading
import time
RLight = False

event = threading.Event()


def RGLight():
    time_period = 0
    event.set()     # 设置标识位
    while True:
        if time_period > 6 and time_period < 11:
            event.clear()   # 清除标志位
            print("\033[31;1m红灯开始。。。!\033[0m")
        elif time_period > 11:
            event.set()     # 设置标识位
            time_period = 0
        else:
            print("\033[34;1m绿灯来啦!\033[0m")
        time.sleep(1)
        time_period += 1


def car(name):
    while True:
        if event.is_set():
            print("%s running"% name)
            time.sleep(1)
        else:
            print("%s waitting" % name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" % name)


lightThread =  threading.Thread(target=RGLight,);
carThread = threading.Thread(target=car,args=("falali",))

lightThread.start()
carThread.start()