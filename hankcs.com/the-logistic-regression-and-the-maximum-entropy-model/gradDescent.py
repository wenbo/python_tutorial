# -*- coding:utf-8 -*-
# Filename: gradDescent.py
# Author：hankcs
# Date: 2015/2/4 15:01
from matplotlib import pyplot as plt
from matplotlib import animation
from numpy import *
 
def loadDataSet():
    """
    加载数据集
 
    :return:输入向量矩阵和输出向量
    """
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])]) #X0设为1.0，构成拓充后的输入向量
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat
 
def sigmoid(inX):
    return 1.0/(1+exp(-inX))
 
def gradAscent(dataMatIn, classLabels, history_weight):
    """
    逻辑斯谛回归梯度上升优化算法
    :param dataMatIn:输入X矩阵（100*3的矩阵，每一行代表一个实例，每列分别是X0 X1 X2）
    :param classLabels: 输出Y矩阵（类别标签组成的向量）
    :return:权值向量
    """
    dataMatrix = mat(dataMatIn)             #转换为 NumPy 矩阵数据类型
    labelMat = mat(classLabels).transpose() #转换为 NumPy 矩阵数据类型
    m,n = shape(dataMatrix)                 #矩阵大小
    alpha = 0.001                           #步长
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):              #最大迭代次数
        h = sigmoid(dataMatrix*weights)     #矩阵内积
        error = (labelMat - h)              #向量减法
        weights += alpha * dataMatrix.transpose() * error  #矩阵内积
        history_weight.append(copy(weights))
    return weights
 
history_weight = []
dataMat,labelMat=loadDataSet()
gradAscent(dataMat, labelMat, history_weight)
fig = plt.figure()
currentAxis = plt.gca()
ax = fig.add_subplot(111)
line, = ax.plot([], [], 'b', lw=2)
 
def draw_line(weights):
    x = arange(-5.0, 5.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]   #令w0*x0 + w1*x1 + w2*x2 = 0，其中x0=1，解出x1和x2的关系
    line.set_data(x, y)
    return line,
 
# initialization function: plot the background of each frame
def init():
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    plt.xlabel('X1'); plt.ylabel('X2');
 
    return draw_line(zeros((n,1)))
 
# animation function.  this is called sequentially
def animate(i):
    return draw_line(history_weight[i])
 
 
# call the animator.  blit=true means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(history_weight), interval=10, repeat=False,
                               blit=False)
plt.show()
anim.save('gradAscent.gif', fps=2, writer='imagemagick')
