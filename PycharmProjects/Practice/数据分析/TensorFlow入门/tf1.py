#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/25 12:50
# software: PyCharm

import tensorflow as tf

#加减乘除
def operation():
    a = tf.constant([3,8])#向量
    b = tf.constant([2,9])
    tf_add = a+b
    tf_mul = a*b
    tf_div= a/b
    tf_sub = a-b
    # tf.add()
    # tf.multiply()
    # tf.div()
    # tf.subtract()

    with tf.Session() as sess: #类型是Tensor就可以在session中运行
        print(sess.run(tf_add))
        print(sess.run(tf_mul))
        print(sess.run(tf_div))
        print(sess.run(tf_sub))

#占位符
def plcaeholder1():
    a = tf.placeholder(tf.int32)
    b = tf.placeholder(tf.int32)
    add = tf.add(a,b)
    mul = tf.multiply(a,b)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer()) # 导尿管有变量（ a = tf.Variable()）时，需要初始化session
        print("加法plcaeholder1: %i" % sess.run(add,feed_dict={a:2,b:3}))


#图
def grapg_test():
    a = tf.constant([1,2])
    b = tf.constant([2,3])
    tf_add = tf.add(a,b)
    #获取默认的图
    graph_default = tf.get_default_graph()
    with tf.Session() as sess:
        print(sess.run(tf_add))

    #构建图
    graph_a = tf.Graph()
    with graph_a.as_default():
        a = tf.constant([3, 4])
        b = tf.constant([2, 3])
        tf_mul = tf.multipy(a,b)
    with tf.Session(graph=graph_a) as sess:
        print("graph run: ",sess.run(tf_mul))

if __name__ == "__main__":

    # hello = tf.constant("Hello TF") #一个Tensor类
    #
    # sess = tf.Session()
    # print(sess.run(hello)) #直接打印hello只能打印Tensor，需要在session中运行，bytes类型
    # sess.run(hello).decode('UTF-8') #解码成UTF-8

    operation()