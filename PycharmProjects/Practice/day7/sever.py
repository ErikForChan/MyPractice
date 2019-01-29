#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/3 17:37
# software: PyCharm
import socket,os

sever = socket.socket()
sever.bind(("localhost",6969))
sever.listen()
print("开始接受数据")
while True:
    coon,addr = sever.accept()
    while True:
        data = coon.recv(1024)
        cmd_res = os.popen(data.decode()).read()
        print("收到数据： "+cmd_res)
        coon.send(cmd_res.encode("UTF-8"))
# coon.send(data)
sever.close()