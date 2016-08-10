# coding=utf-8

import math
from numpy import *
import matplotlib.pyplot as plt
import matplotlib

def loadDataSet(fileName):
    """
    加载数据集
    :param fileName:
    :return:
    """
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

#计算权值,w=sum(alpha*label*x)  
def calcWs(alphas,dataArr,classLabels):  
    X = mat(dataArr); labelMat = mat(classLabels).transpose()  
    m,n = shape(X)  
    w = zeros((n,1))  
    for i in range(m):  
        w += multiply(alphas[i]*labelMat[i],X[i,:].T)  
    return w  

def selectJrand(i,m):
    """
    随机从0到m挑选一个不等于i的数
    :param i:
    :param m:
    :return:
    """
    j=i             #排除i
    while (j==i):
        j = int(random.uniform(0,m))
    return j
 
def clipAlpha(aj,H,L):
    """
    将aj剪裁到L(ow)和H(igh)之间
    :param aj:
    :param H:
    :param L:
    :return:
    """
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    """
    简化版SMO算法
    :param dataMatIn:       X
    :param classLabels:     Y
    :param C:               惩罚参数
    :param toler:           容错率
    :param maxIter:         最大循环次数
    :return:
    """
    dataMatrix = matrix(dataMatIn); labelMat = matrix(classLabels).transpose()
    b = 0; m,n = shape(dataMatrix)  # m:=训练实例的个数；n:=每个实例的维度
    alphas = mat(zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0   #alpha是否已经进行了优化
        for i in range(m):
            #   w = alpha * y * x;  f(x_i) = w^T * x_i + b
            fXi = float(multiply(alphas,labelMat).T*dataMatrix*dataMatrix[i,:].T) + b     # 预测的类别
            Ei = fXi - float(labelMat[i])   #得到误差，如果误差太大，检查是否可能被优化
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)): #必须满足约束
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy()                # 教材中的α_1^old和α_2^old
                if (labelMat[i] != labelMat[j]):                                          # 两者所在的对角线段端点的界
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H: print "L==H"; continue
                # Eta = -(2 * K12 - K11 - K22)，且Eta非负，此处eta = -Eta则非正
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print "eta>=0"; continue
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                #如果内层循环通过以上方法选择的α_2不能使目标函数有足够的下降，那么放弃α_1
                if (abs(alphas[j] - alphaJold) < 0.00001): print "j not moving enough"; continue
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1
                print "iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged)
        if (alphaPairsChanged == 0): iter += 1
        else: iter = 0
        print "iteration number: %d" % iter
    return b,alphas

def plotSVM(dataArr, labelArr, w, b, svList):
    xcord0 = []
    ycord0 = []
    xcord1 = []
    ycord1 = []
    markers =[]
    colors =[]
    for i in range(len(labelArr)):
        xPt = dataArr[i][0]
        yPt = dataArr[i][1]
        label = labelArr[i]
        if (label == -1):
            xcord0.append(xPt)
            ycord0.append(yPt)
        else:
            xcord1.append(xPt)
            ycord1.append(yPt)
 
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord0,ycord0, marker='s', s=90)
    ax.scatter(xcord1,ycord1, marker='o', s=50, c='red')
    plt.title('Support Vectors Circled')
    for sv in svList:
        circle = matplotlib.patches.Circle((dataArr[sv][0], dataArr[sv][1]), 0.5, facecolor='none', edgecolor=(0,0.8,0.8), linewidth=3, alpha=0.5)
        ax.add_patch(circle)
 
    w0=w[0][0]; w1=w[1][0]; b=float(b)
    x = arange(-2.0, 12.0, 0.1)
    y = (-w0*x - b)/w1
    ax.plot(x,y)
    ax.axis([-2,12,-8,6])
    plt.show()


dataArr, labelArr = loadDataSet('testSet.txt')
b,alphas = smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print b
w = calcWs(alphas, dataArr, labelArr)
print w
svList = []
for i in range(len(alphas)):
    if abs(alphas[i]) > 0.0000001 :
        print dataArr[i], labelArr[i]
        svList.append(i)
 
plotSVM(dataArr, labelArr, w, b, svList)
