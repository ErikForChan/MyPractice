#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/3 17:35
# software: PyCharm
import socket
client = socket.socket()
client.connect(("localhost",6969))
while True:
    msg = input("我要发数据>>:").strip()
    print("开始发送数据: "+msg)
    client.send(msg.encode("UTF-8"))
    data = client.recv(1024)
    print("客户端接受数据：  "+data.decode())
client.close()
