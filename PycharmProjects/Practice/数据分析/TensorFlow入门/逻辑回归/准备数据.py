#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/25 18:18
# software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

train_x = np.linspace(-1,1,100)

# *train_x.shape 把元组解开
train_y = 100 * train_x + np.random.randn(*train_x.shape) *0.5
plt.plot(train_x,train_y,'bo',label="data")
plt.legend()
plt.show()

