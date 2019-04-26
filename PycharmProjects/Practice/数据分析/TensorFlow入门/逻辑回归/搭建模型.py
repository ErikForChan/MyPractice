#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/26 10:48
# software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

X = tf.placeholder("float")
Y = tf.placeholder("float")

W = tf.Variable(tf.random_normal([1]),name="Weight")
b = tf.Variable(tf.zeros([1]),name="Bias")

#向前结构
z = tf.multiply(X,W) + b
#反向优化
#平均值（平方差（Y-z））
cost = tf.reduce_mean(tf.square(Y-z))


learning_rate = 0.01 #学习率
#梯度下降法
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) #找到cost最小的值



