#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/28 18:33
# software: PyCharm

import tensorflow as tf
import numpy as np

x_data = np.random.rand(100)
y_data = x_data*0.1+0.2

#构造一个线性模型,用于接近以上的样本
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b

#二次代价函数
loss = tf.reduce_mean(tf.square(y_data - y)) #平均值（平方(真实值-预测值)）
#梯度下降法来训练的优化器
optimizer = tf.train.GradientDescentOptimizer(0.2)
#最小化代价函数
train = optimizer.minimize(loss) #loss越小，结果越接近真实值

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        # print("loss: " + str(sess.run(loss)))
        if step%10 == 0:
            print(sess.run([k,b]))
