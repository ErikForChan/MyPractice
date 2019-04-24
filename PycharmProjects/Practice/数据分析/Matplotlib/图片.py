#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/24 12:02
# software: PyCharm

import matplotlib.pyplot as plt
import numpy as np

#伪图片
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='low')
plt.colorbar(shrink=0.7) #shrink 压缩

plt.xticks(())
plt.yticks(())
plt.show()
