#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/11 9:26
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170910_03.py
'''
@Description:
阅读《统计学习方法》(如果你没有纸质书的话，群文件里有这本书的电子版)第二章：感知机。然后解答如下问题:
已知二维平面有一组点:(0,0),(0,1),(0.5,0.3),(0.2,0.8),(1.2,2.4),(1.5,1.5),(2,2),(2.5,3) 共8个点，前4个点为一类，后4个点为一类，利用感知器
算法求出将这两类点划分开来的直线的方程。
'''
import matplotlib.pyplot as plt

def sign(x):
    return 1 if x>0 else -1

points = [(0,0),(0,1),(0.5,0.3),(0.2,0.8),(1.2,2.4),(1.5,1.5),(2,2),(2.5,3)] # 8个点
classify = (-1,-1,-1,-1,1,1,1,1) # -1 和 +1 分别为两类
alpha = 0.1 # 学习率
w0 = [1.,1.] # 初始w
b0 = 1. # 初始b
count = 0 # 正确分类点的个数
while(count < 8):
    count = 0
    for i in range(8):
        if(sign(w0[0]*points[i][0] + w0[1]*points[i][1] + b0)*classify[i] == -1):
            w0[0] += alpha*points[i][0]*classify[i]
            w0[1] += alpha*points[i][1]*classify[i]
            b0 += alpha*classify[i]
        else:
            count += 1

# 用图形展示分类的结果
X = [v[0] for v in points] # X坐标列表
Y = [v[1] for v in points] # Y坐标列表
plt.plot(X,Y,'r*')
lineX = [i*0.01 for i in range(300)]
lineY = [-(w0[0]*x + b0)/w0[1] for x in lineX]
plt.plot(lineX,lineY,'g.') # 画线
plt.show()
