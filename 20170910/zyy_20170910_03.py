# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-2017091003 感知器算法"
"""
感知机模型假设:数据集是线性可分的

lost function：所有误分类点到超平面的距离和

利用随机梯度下降法进行优化
 
感知机算法，有原始形式以及对偶形式
"""
x1=[0,0,0.5,0.2,1.2,1.5,2,2.5]
x2=[0,1,0.3,0.8,2.4,1.5,2,3]
y=[-1,-1,-1,-1,1,1,1,1]

x  = list(zip(x1,x2))
import numpy as np
x = np.array(x)
y = np.array(y)

def sign(x):
    return 1 if x>0 else -1
    
def Perceptron1(a,w,b,x):
    #感知机学习算法的原始形式
    # a : learning rate
    # w,b:variable
    # x: test set
    for i in range(0,len(x)):
        l = (np.dot(x[i],w)+b)*y[i]  #np.dot 点乘
        if sign(l) == -1:
            w = w + a*y[i]*x[i]          
            b = b + a*y[i]
            w, b = Perceptron1(a,w,b,x)            
    return w,b

def Perceptron2(a,b,x):
    #感知机学习算法的对偶形式
    #计算Gram矩阵    
    G =[]
    x = np.mat(x)
    G = x*x.T
    for i in range(0,len(x)):
        l = (np.mat(a*y)*G[i].T + b) * y[i]
        if sign(l) == -1:
            a[i] +=1
            b += y[i]
            a,b,w= Perceptron2(a,b,x)
    w = np.mat(a*y)*x
    w = w.tolist()[0]
    return a,b,w
    
w = np.array([0.5,2])  #初始w
b = 1  #初始b
a = 0.5  #learning rate
w1, b1= Perceptron1(a,w,b,x) #使用原始形式
print(w1,b1)
linex1 = np.array([0,2.5]) #用于绘制分割线两个点x的坐标
liney1 = -w1[0]/w1[1]*linex1 - b1/w1[1] #用于绘制分割线两个点y的坐标
import matplotlib.pyplot as plt
plt.scatter(x1,x2)
plt.plot(linex1,liney1,'r')

a0 = np.zeros(len(x)) #初始化a
#a0 =[1,2,1,0,0,0,0,0]
b0 = 0 
a2,b2,w2 = Perceptron2(a0,b0,x) #使用对偶形式
print(w2,b2)
linex2 = np.array([0,2.5]) #用于绘制分割线两个点x的坐标
liney2 = -w2[0]/w2[1]*linex2 - b2/w2[1]
plt.plot(linex2,liney2,'b')

"""
评价：该算法根据初始值的不同，得到的结果也不同，并且差异很大
"""
