# -*- coding:utf-8 -*-
# Filename: dimensionality.py
# Author：hankcs
# Date: 2015/2/6 14:40
from matplotlib import pyplot as plt
import numpy as np
 
max_dimensionality = 10
ax = plt.axes(xlim=(0, max_dimensionality), ylim=(0, 1 / (0.01 ** max_dimensionality)))
x = np.linspace(0, max_dimensionality, 1000)
y = 1 / (0.01 ** x)
plt.plot(x, y, lw=2)
plt.show()
