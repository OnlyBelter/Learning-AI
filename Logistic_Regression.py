# 逻辑回归
'''
Created on Oct 27, 2010
Logistic Regression Working Module
@author: Peter

Altered on Dec 26, 2016
@author: Belter
'''
from numpy import *
import os

path = 'D:\MechineLearning\MLiA_SourceCode\machinelearninginaction\Ch05'
training_sample = 'trainingSample.txt'
testing_sample = 'testingSample.txt'



def loadDataSet(p, file_n):
    dataMat = []; labelMat = []
    fr = open(os.path.join(p, file_n))
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  # x0 = 1
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
    labelMat = mat(classLabels).transpose() #convert to NumPy matrix
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 1000
    weights = ones((n,1))
    for k in range(maxCycles):              # heavy on matrix operations
        h = sigmoid(dataMatrix*weights)     # matrix multiplication
        error = (labelMat - h)              # vector subtraction
        temp = dataMatrix.transpose()* error # matrix multiplication
        weights = weights + alpha * temp  # 同梯度上升法
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet(path, training_sample)
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

def test_logistic_regression():
    dataArr, labelMat = loadDataSet(path, training_sample)
    A = gradAscent(dataArr, labelMat)
    h = sigmoid(mat(dataArr)*A)
    print(dataArr, labelMat)
    print(A)
    print(h)
    # plotBestFit(A.getA())

def predict_test_sample():
    A = [5.262118, 0.60847797, -0.75168429]
    dataArr, labelMat = loadDataSet(path, testing_sample)
    h_test = sigmoid(mat(dataArr) * mat(A).transpose())
    print(h_test)


test_logistic_regression()
predict_test_sample()
