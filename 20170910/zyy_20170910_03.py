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

def Perceptron2(a,w,b,x):
    #感知机学习算法的对偶形式(未完成)
    #计算Gram矩阵 
    G = []
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            G[i][j] = np.dot(x[i],x[j])
    
w = np.array([0.5,2])  #初始w
b = 1  #初始b
a = 0.5  #learning rate
w0, b0= Perceptron1(a,w,b,x) #使用原始形式
print(w0,b0)
linex = np.array([0,2.5]) #用于绘制分割线两个点x的坐标
liney = -w0[0]/w0[1]*linex - b0/w0[1] #用于绘制分割线两个点y的坐标
import matplotlib.pyplot as plt
plt.scatter(x1,x2)
plt.plot(linex,liney,'r')

"""
评价：该算法根据初始值的不同，得到的结果也不同，并且差异很大
"""
