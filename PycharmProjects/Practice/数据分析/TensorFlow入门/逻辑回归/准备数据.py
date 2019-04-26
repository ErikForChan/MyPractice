#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/25 18:18
# software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.tools.inspect_checkpoint import  print_tensors_in_checkpoint_file
#获取10个数的平均值
def moving_average(a,w=10):
    if len(a) < w:
        return a[:]
    return [val if idx<w else sum(a[(idx-w):idx])/w for idx,val in enumerate(a)]

train_x = np.linspace(-1,1,100)
test_X = np.linspace(-0.5,0.8,30)
# *train_x.shape 把元组解开
train_y = 8 * train_x + np.random.randn(*train_x.shape) *0.5
plt.plot(train_x,train_y,'bo',label="data")
# plt.legend()
# # plt.show()
print("######搭建模型#########")
###搭建模型
inputdict = {
    'x': tf.placeholder("float"),
    'y': tf.placeholder("float")
}

W = tf.Variable(tf.random_normal([1]),name="Weight")
b = tf.Variable(tf.zeros([1]),name="Bias")

#正向搭建
z = tf.multiply(inputdict['x'], W)+ b
tf.summary.histogram("z",z)
#反向优化
#平均值（平方差（Y-z））
cost =tf.reduce_mean( tf.square(inputdict['y'] - z))
tf.summary.scalar("loss_function",cost)
learning_rate = 0.01 #学习率
#梯度下降法
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost) #找到cost最小的值


######迭代训练模型#########
print("######迭代训练模型#########")
init = tf.global_variables_initializer()
epochs = train_x.size
print(epochs)
setp = 30

saver = tf.train.Saver() #保存最新的
saverdir = "./model_dir/"
model_file = saverdir + "linermodel"
plotdata = {"batchsize":[],"loss":[]}
isTrain= True


with tf.Session() as sess:
    sess.run(init)
    # ckpt = tf.train.get_checkpoint_state(saverdir) #模型检查点保存
    #合并所有的summary
    memged_summary_op = tf.summary.merge_all()
    summary_writer = tf.summary.FileWriter("log/log_summary",sess.graph) #加入图

    if isTrain:
        for epoch in range(epochs):
            for(x,y) in zip(train_x,train_y):
                sess.run(optimizer, feed_dict={inputdict['x']: x, inputdict['y']: y})
            summary_str = sess.run(memged_summary_op,feed_dict={inputdict['x']:x,inputdict['y']:y})
            summary_writer.add_summary(summary_str,epoch)
            if epoch % setp == 0:
                loss = sess.run(cost, feed_dict={inputdict['x']: train_x, inputdict['y']: train_y})
                if not (loss == "NA"):
                    plotdata["batchsize"].append(epoch)
                    plotdata["loss"].append(loss)

        saver.save(sess,model_file,global_step=epoch)
        # for x in zip(test_X):
        #     print("x= ",x,"  z= ",sess.run(z,feed_dict={X:x}))
    else:
        saver.restore(sess,model_file)
        print_tensors_in_checkpoint_file(
            model_file,
            None,
            True
        )
        print("cost=", sess.run(cost, feed_dict={inputdict['x']: train_x, inputdict['y']: train_y}), "W=", sess.run(W),
              "b=", sess.run(b))


    print("  #######图形展示########")
    plt.plot(train_x,train_y,'ro',label="Orignal data")
    plt.plot(train_x,sess.run(W)*train_x+sess.run(b),label="Fittedline")

    plt.plot(test_X,sess.run(W)*test_X+sess.run(b),'co',label="TestLine")
    plt.legend()
    plt.show()

    plotdata["avgloss"] = moving_average(plotdata["loss"])

    plt.figure(1)
    plt.subplot(211)
    plt.plot(plotdata["batchsize"],plotdata["avgloss"],'b--')
    plt.xlabel("Minibatch number")
    plt.ylabel("Loss")
    plt.title("Minibatch sun vs.Traininf loss")
    plt.show()

    print("x=0.2，z=", sess.run(z, feed_dict={inputdict['x']: 0.2}))
