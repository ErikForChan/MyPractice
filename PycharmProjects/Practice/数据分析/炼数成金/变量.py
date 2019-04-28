#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/28 13:16
# software: PyCharm

import tensorflow as tf

a = tf.constant([[3,3]])
b = tf.constant([[2],[3]])

op = tf.matmul(a,b)

#定义一个会话，启动默认图
sess = tf.Session()
state = tf.Variable(0,name="counter")
new_value = tf.add(state,1)
update = tf.assign(state.new_value)
init = tf.global_variables_initializer()
# res = sess.run(op)
# print(res)
# sess.close()

with tf.Session() as sess:
    sess.run(init)
    res = sess.run(op)
    print(res)
    for i in range(5):
        sess.run(update)
        print(sess.run(state))

