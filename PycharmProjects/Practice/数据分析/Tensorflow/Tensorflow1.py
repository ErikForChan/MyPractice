#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/22 17:21
# software: PyCharm
import tensorflow as tf
import numpy as np

#创建数据
x_data = np.random.rand(100).astype(np.float64)
y_data = x_data*0.1+0.3
# print(x_data)
# print(y_data)

#开始创建结构
Weights = tf.Variable(tf.random_uniform([1],-1,1)) #一维的结构，在-1到1之间
biase = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biase

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5) #较少误差
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biase))
