#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/28 18:51
# software: PyCharm

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis] #均匀分布的200个点

noise = np.random.normal(0,0.02,x_data.shape)
y_data = np.square(x_data) + noise

x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

#定义神经网络中间层
Weight1 = tf.Variable(tf.random.normal([1,10]))
biases = tf.Variable(tf.zeros([1,10]))
plus1 = tf.matmul(x,Weight1) + biases
L1 = tf.nn.tanh(plus1)

#定义神经网络输出层
Weight2 = tf.Variable(tf.random_normal([10,1]))
biases2 = tf.Variable(tf.zeros([1,1]))
plus2 = tf.matmul(L1,Weight2) + biases2
prediction = tf.nn.tanh(plus2)

loss = tf.reduce_mean(tf.square(y-prediction))
optimizer = tf.train.GradientDescentOptimizer(0.2)
train = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        sess.run(train,feed_dict={x:x_data,y:y_data})

    #获得预测值
    value = sess.run(prediction,feed_dict={x:x_data})

    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,value,'r--',lw=5)
    plt.show()