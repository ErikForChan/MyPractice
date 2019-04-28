#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/28 18:26
# software: PyCharm
import tensorflow as tf

# Fetch 运行多个op,并得到运行的结果
a1 = tf.constant(3.0)
a2 = tf.constant(2.0)
a3 = tf.constant(5.0)

add = tf.add(a1,a2)
mul = tf.multiply(a1,add)

with tf.Session() as sess:
    res = sess.run([mul,add])
    print(res)


#feed给占位符加数据


