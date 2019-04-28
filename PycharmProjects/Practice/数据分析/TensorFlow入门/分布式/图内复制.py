#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/28 9:54
# software: PyCharm

import tensorflow as tf
from time import  sleep

var = tf.Variable(3.0,name="var1")

server = tf.train.Server.create_local_server() #全局的server,seession放在期中后，只需要一个sess初始化就可以

sess1 = tf.Session(server.target)
sess2 = tf.Session(server.target)
sess1.run(tf.global_variables_initializer())

print("session1:  ",sess1.run(var))
print("session2:  ",sess2.run(var))

