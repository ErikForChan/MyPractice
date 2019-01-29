#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/7 10:16
# software: PyCharm
import threading
import time

#线程锁
lock = threading.Lock()

#  我定义的线程类
class MyThread(threading.Thread):

    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        # lock.acquire()
        print("Thread--"+self.num,end='\n')
        time.sleep(2)
        # lock.release()


thread_lists =[]
for i in range(100):
    t = MyThread("t"+str(i))
    t.setDaemon(True)   # 设置守护线程
    t.start()
    # t.run()
    thread_lists.append(t)

for t in thread_lists:
    t.join()

t1 = MyThread("t1")
t2 = MyThread("t2")

t1.run()
t2.run()

