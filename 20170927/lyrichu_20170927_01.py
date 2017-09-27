#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170927_01.py
@time: 2017/9/26 16:27
@description:
设计一种算法，给定数a和数b(a<b),生成服从(a,b)间均匀分布的随机数。在已知均匀分布的情况下，如果已知概率密度函数，如何生成服从该分布的
随机数？试以正态分布的情况为例进行说明。
"""
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
import time
import math

def uniform(down,up,x0=int(time.time()),num=1,a = 1103515245,b=12345,m=2**31):
    '''
    这里使用最简单且广泛使用的线性同余法来产生均匀分布的随机数
    参考:http://blog.csdn.net/jackytintin/article/details/7798157
    :param down: 下界
    :param up：上界
    :param x0:随机数种子，默认使用当前系统时间戳(取整)作为随机数种子
    :param num:产生随机数的个数
    :param a:参数a
    :param b:参数b
    :param m:参数m
    :return:[down,up]之间的服从均匀分布的(伪)随机数
    '''
    # 服从均匀分布的随机数列表
    uniformList = []
    for i in range(num):
        x1 = (a*x0 + b) % m
        # 将随机数映射到 [up,down]上
        x1_norm = (float(x1)/m)*(up-down) + down
        uniformList.append(x1_norm)
        x0 = x1
    return uniformList

def generateDistribution(pdf,pdfMin,pdfMax,xMin,xMax,num = 1):
    '''
    根据均匀分布产生任意分布的随机数
    注意这里使用的线性同余法对于参数是非常敏感的
    这里的第一组参数a1,b1,m1使用的c语言默认的参数
    第二组参数是多次尝试以后根据经验取得参数
    :param pdf: 分布的密度函数
    :param pdfMin:密度函数的最小值
    :param pdfMax: 密度函数的最大值
    :param xMin:x的最小值
    :param xMax：x的最大值
    :param num: 产生随机数的数量
    :return: 产生的随机数列表
    '''
    # 指定分布随机数的列表
    distributionList = []
    # a1,b1,m1是生成x均匀分布随机数的参数
    a1 = 1103515245
    b1=12345
    m1=2**31
    # a2,b2,m2 是生成y均匀分布随机数的参数
    a2 = 1234576980
    b2 = 15423
    m2 = 2**31
    # 初始化随机数种子
    x0 = int(time.time())
    y0 = x0
    for i in range(num):
        while(True):
            # x,y的标准化
            x1 = (a1*x0+b1) % m1
            x1_norm = (float(x1)/m1)*(xMax-xMin) + xMin
            y1 = (a2*y0+b2) % m2
            y1_norm = (float(y1)/m2)*(pdfMax-pdfMin) + pdfMin
            # 更新x、y的值
            x0 = x1
            y0 = y1
            if(pdf(x1_norm) > y1_norm):
                distributionList.append(x1_norm)
                break
    # 返回分布列表
    return distributionList

def normalDistributionPdf(x):
    '''
    标准正态分布密度函数
    :param x: x值
    :return: 对应的y值
    '''
    y = (1./(math.sqrt(2*math.pi)))*math.exp(-x*x/2)
    return y


if __name__ == '__main__':
    down = 1
    up = 2
    # 均匀分布随机数的个数
    uniformNum = 10
    # 产生均匀分布的随机数在[down,up]之间
    uniformList = uniform(down=down,up =up,num=uniformNum)
    print(uniformList)
    # 生成指定分布的随机数,这里指定为标准正态分布
    # 密度函数最小值
    pdfMin = 0
    # 密度函数最大值
    pdfMax = 1./(math.sqrt(2*math.pi))
    # x最小值
    xMin = -3
    # x最大值
    xMax = 3
    # 标准正态分布随机数的个数
    normalNum = 100
    normalDistributionList = generateDistribution(pdf=normalDistributionPdf,pdfMin=pdfMin,
                                                  pdfMax=pdfMax,xMin=xMin,xMax=xMax,num=normalNum)
    print(normalDistributionList)
    # 画出模拟的标准正态分布的密度曲线
    Y = [normalDistributionPdf(x) for x in normalDistributionList]
    plt.plot(normalDistributionList,Y,'r.')
    plt.title(r'$y=\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$')
    plt.show()






