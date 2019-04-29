#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/29 10:10
# software: PyCharm

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MINIST_data",one_hot=True) #one_hot某一位为1，其他都为0

batch_size = 100 #训练模型时一次放入100张图片，以矩阵的形式
n_batch = mnist.train.num_examples #计算一共多少批次
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#一个简单的神经网络
W = tf.Variable(tf.zeros([784,10]))
biases = tf.Variable(tf.zeros([10]))
pre = tf.nn.softmax(tf.matmul(x,W)+biases)

#二次代价函数
# loss = tf.reduce_mean(tf.square(y-pre))
#对数释然函数，交叉熵 比二次代价函快
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=pre))
train = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
init = tf.global_variables_initializer()

#bool型列表
correct_pre = tf.equal(tf.argmax(y,1),tf.argmax(pre,1)) #argmax:最大值的位置 预测的值和真实值的最大值是否在同一个位置
accuracy = tf.reduce_mean(tf.cast(correct_pre,tf.float32))
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch): #把所有的图片训练一次
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train,feed_dict={x:batch_xs,y:batch_ys})

        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Turn: "+str(epoch)+",Acc: "+str(acc))


