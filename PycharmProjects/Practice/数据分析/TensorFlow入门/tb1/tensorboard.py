#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/25 15:53
# software: PyCharm

import tensorflow as tf

with tf.name_scope("INPUT_OP"):
    a = tf.Variable(30,name="INPUTA")
    b = tf.Variable(36, name="INPUTB")

# tensorboard --logdir logdir
#后台运行 nohup tensorboard --logdir logdir/
with tf.name_scope("ADD_OP"):
    tf_add = tf.add(a,b,name="TF_ADD")

with tf.name_scope("SUB_OP"):
    tf_sub = tf.subtract(a,b,name="TF_SUB")

with tf.name_scope("DIV_OP"):
    tf_div = tf.div(a,b,name="TF_DIV")

with tf.name_scope("MUL_OP"):
    tf_mul = tf.multiply(a,b,name="TF_ADD")

with tf.Session(graph=tf.get_default_graph()) as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf_add)
    sess.run(tf_sub)
    sess.run(tf_mul)
    sess.run(tf_div)
    summary_writer = tf.summary.FileWriter("logs",sess.graph)