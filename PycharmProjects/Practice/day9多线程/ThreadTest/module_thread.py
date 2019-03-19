#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/7 10:16
# software: PyCharm
import time
import threading
#线程锁
lock = threading.Lock()

#  我定义的线程类
class MyThread(threading.Thread):

    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        # lock.acquire()
        time.sleep(2)
        print("Thread--"+self.num,end='\n')
        # time.sleep(2)
        # lock.release()


if __name__ == '__main__':
    print('这是主线程：', threading.current_thread().name)
    # t1 = MyThread("LLL1")
    # t2 = MyThread("LLL2")

    # t1.run()
    # t2.run()
    thread_lists = []
    for i in range(100):
        t = MyThread("t" + str(i))
        # t.run()
        thread_lists.append(t)

    # join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止,就像变成串行
    for t in thread_lists:
        t.setDaemon(True)  # 设置守护线程:没有执行完时，主线程可以结束
        t.start()
        t.join()

    print('主线程结束了！', threading.current_thread().name)

