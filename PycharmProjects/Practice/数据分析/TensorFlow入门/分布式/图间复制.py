#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/28 10:19
# software: PyCharm

import tensorflow as  tf
from multiprocessing import Process
from  time import sleep
#一个服务器用来保存所有参数，另一个服务器用来计算

# 定义集群参数
cluster = tf.train.ClusterSpec({
    "worker": [
        "localhost:3333",
        "localhost:3334",
    ],
    "ps": [
        "localhost:3335"
    ]
})


# 定义一个参数服务器
def parameter_server():
    with tf.device("/job:ps/task:0"):
        var = tf.Variable(0.0, name='var')

    server = tf.train.Server(cluster,
                             job_name="ps",
                             task_index=0)
    sess = tf.Session(target=server.target)

    print("Parameter server: waiting for cluster connection...")
    sess.run(tf.report_uninitialized_variables()) #等待初始化
    print("Parameter server: cluster ready!")

    print("Parameter server: initializing variables...")
    sess.run(tf.global_variables_initializer())
    print("Parameter server: variables initialized")

    for i in range(5):
        val = sess.run(var)
        print("Parameter server: var has value %.1f" % val)
        sleep(1.0)

    print("Parameter server: blocking...")
    server.join()


# 定一个Worker,进行计算
def worker(worker_n):
    with tf.device("/job:ps/task:0"):
        var = tf.Variable(0.0, name='var')

    server = tf.train.Server(cluster,
                             job_name="worker",
                             task_index=worker_n)
    sess = tf.Session(target=server.target)

    print("Worker %d: waiting for cluster connection..." % worker_n)
    sess.run(tf.report_uninitialized_variables())
    print("Worker %d: cluster ready!" % worker_n)

    while sess.run(tf.report_uninitialized_variables()):
        print("Worker %d: waiting for variable initialization..." % worker_n)
        sleep(1.0)
    print("Worker %d: variables initialized" % worker_n)

    for i in range(5):
        print("Worker %d: incrementing var" % worker_n)
        sess.run(var.assign_add(1.0))
        sleep(1.0)

    print("Worker %d: blocking..." % worker_n)
    server.join()


ps_proc = Process(target=parameter_server, daemon=True)
w1_proc = Process(target=worker, args=(0,), daemon=True)
w2_proc = Process(target=worker, args=(1,), daemon=True)

ps_proc.start()
w1_proc.start()
w2_proc.start()
sleep(20)
for proc in [w1_proc, w2_proc, ps_proc]:
    proc.terminate()

