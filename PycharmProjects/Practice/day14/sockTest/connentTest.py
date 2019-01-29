#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/17 14:55
# software: PyCharm

import socket
import time


def handle_request(client):
    buf = client.recv(1024)
    client.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    f = open('index.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    r = str(time.time())
    data.replace('@@@@@',r)
    client.send(bytes(data,encoding="utf-8"))


def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)

    while True:
        conn,add = sock.accept()
        handle_request(conn)
        conn.close()


if __name__ == '__main__':
    main()
