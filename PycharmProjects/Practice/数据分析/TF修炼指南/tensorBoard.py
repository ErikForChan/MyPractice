#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/25 15:40
# software: PyCharm

import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

INPUT_NODE=784
OUTPUT_NODE=10
LAYER1_NODE=500
def get_weight_variable(shape,regularizer):
    weights=tf.get_variable('weights',shape,initializer=tf.truncated_normal_initializer(stddev=0.1))
    if regularizer !=None:
        tf.add_to_collection('losses',regularizer(weights))
    return weights

def inference(input_tensor,regularizer):
    with tf.variable_scope('layer1',reuse=tf.AUTO_REUSE):
        weights=get_weight_variable([INPUT_NODE,LAYER1_NODE],regularizer)
        biases=tf.get_variable('biases',[LAYER1_NODE],initializer=tf.constant_initializer(0.0))
        layer1=tf.nn.relu(tf.matmul(input_tensor,weights)+biases)
    with tf.variable_scope('layer2',reuse=tf.AUTO_REUSE):
        weights=get_weight_variable([LAYER1_NODE,OUTPUT_NODE],regularizer)
        biases=tf.get_variable('biases',[OUTPUT_NODE],initializer=tf.constant_initializer(0.0))
        layer2=tf.matmul(layer1,weights)+biases
    return layer2

#配置神经网络参数
LAYER1_NODE=500
BATCH_SIZE=100
LEARNING_RATE_BASE=0.8
LEARNING_RATE_DECAY=0.99
REGULARIZTION_RATE=0.0001
TRAINING_STEPS=3000
MOVING_AVERAGE_DECAY=0.99
#模型保存的路径和文件名
MODEL_SAVE_PATH='/path/to/'
MODEL_NAME='model.ckpt'
def train(mnist):
    with tf.name_scope('input'):
        x=tf.placeholder(tf.float32,[None,INPUT_NODE],name='x-input')
        y_=tf.placeholder(tf.float32,[None,OUTPUT_NODE],name='y-input')
    regularizer=tf.contrib.layers.l2_regularizer(REGULARIZTION_RATE)
    #y=mnist_inference.inference(x,regularizer)
    y=inference(x,regularizer)
    global_step=tf.Variable(0,trainable=False)
    with tf.name_scope('moving_averages'):
        variable_averages=tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
        variable_averages_op=variable_averages.apply(tf.trainable_variables())
    with tf.name_scope('loss_function'):
        cross_entropy=tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,labels=tf.argmax(y_,1))
        cross_entropy_mean=tf.reduce_mean(cross_entropy)
        loss=cross_entropy_mean+tf.add_n(tf.get_collection('losses'))
    with tf.name_scope('train_step'):
        learning_rate=tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,mnist.train.num_examples/BATCH_SIZE,LEARNING_RATE_DECAY)
        train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step=global_step)
        train_op=tf.group(train_step,variable_averages_op)
#初始化tensorflow持久类
    tf.summary.scalar("loss",loss)
    tf.summary.scalar("learningRate",learning_rate)
    for var in tf.trainable_variables():
        tf.summary.histogram(var.name, var)
# Merge all summaries into a single op
    merged_summary_op = tf.summary.merge_all()
    saver=tf.train.Saver()
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        train_writer = tf.summary.FileWriter("/path/to/log",sess.graph)
        for i in range(1,TRAINING_STEPS+1):
            xs,ys=mnist.train.next_batch(BATCH_SIZE)
            #记录每一个节点的信息
            if i % 1000 ==0:
                saver.save(sess,os.path.join(MODEL_SAVE_PATH,MODEL_NAME),global_step=global_step)
                run_options=tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
                run_metadata=tf.RunMetadata()
                _,loss_value,step=sess.run([train_op,loss,global_step],feed_dict={x:xs,y_:ys},
                                          options=run_options,run_metadata=run_metadata)
                train_writer.add_run_metadata(run_metadata,'step%03d' % i)
                print('After %d training step(s), loss on training batch is %g.' % (step, loss_value))
            else:
                _,loss_value,step,summary=sess.run([train_op,loss,global_step,merged_summary_op],feed_dict={x:xs,y_:ys})
                train_writer.add_summary(summary, i)
        train_writer.close()
def main(argv=None):
    mnist=input_data.read_data_sets('/tmp/data',one_hot=True)
    train(mnist)
if __name__=='__main__':
    tf.app.run()

