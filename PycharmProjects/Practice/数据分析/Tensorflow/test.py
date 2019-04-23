#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/23 14:24
# software: PyCharm
# import tensorflow as tf
#
# b = tf.Variable(tf.zeros([100]))
# # print(b)
# w = tf.Variable(tf.random_uniformn([700,100],-1,1))
# x = tf.placeholder(name='x')
# relu = tf.nn.relu(tf.matmul(w,x)+b)
# c = [...]
#
# s= tf.Session()
# for step in range(0,10):
#     res = s.run(c,feed_dict={x:})
#     print(step,res)