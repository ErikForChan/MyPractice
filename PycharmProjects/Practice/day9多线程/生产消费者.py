#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/10 12:50
# software: PyCharm

import threading,time
import queue

#定义一个最大长度为10的队列
q= queue.Queue(maxsize=10)

#生产者
def Producer(name):
    count = 1
    while True:
        q.put("面包%s"%count)
        print("生产了面包", count)
        count += 1
        time.sleep(0.2)


#消费者
def Consumer(name):
    while True:
        print("[%s] 吃了[%s] ..." % (name, q.get()))
        time.sleep(1)


#生产者对象Jack
p = threading.Thread(target=Producer,args=("Jack",))
#消费者对象Mary
p2 = threading.Thread(target=Consumer,args=("Mary",))
#消费者对象Alice
p3 = threading.Thread(target=Consumer,args=("Alice",))

p.start()
p2.start()
p3.start()