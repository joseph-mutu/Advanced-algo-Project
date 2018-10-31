#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 13:56:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np
import ExtractData as ED


# 以下代码用来添加坐标轴

Cormat,numC = ED.PreData()
X_C = Cormat[:,1] # 城市的横坐标
Y_C = Cormat[:,2] # 城市的纵坐标

fig = plt.figure(figsize = (14,8))
plt.plot(X_C,Y_C,'or',markersize = 5)
plt.show()

# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(224)

# x = np.linspace(0,np.pi)
# y_cos = np.cos(x)
# y_sin = np.sin(x)

# ax1.plot(x,y_sin)
# ax2.plot(x,y_cos)

# plt.show()

