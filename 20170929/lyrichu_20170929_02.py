#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170929_02.py
@time: 2017/9/29 14:10
@description:圆周率pi有很多高精度的算法，试自行查阅资料，实现一种算法将圆周率pi计算到小数点后一万位。
"""
from __future__ import division,print_function
import math
# 注意这里需要使用 python 高精度计算模块 decimal
from decimal import *

def product(k):
    '''
    计算 k的阶乘
    :param k: k>=0
    :return: k!
    '''
    return 1 if k==0 else reduce(lambda x,y:x*y,range(1,k+1))

def arctan(x,k):
    '''
    计算反正切 arctan,使用泰勒展开
    :param x: x弧度
    :param k: 展开项数
    :return: 计算结果
    '''
    index = Decimal(1)
    res = Decimal(0)
    while(index <= k):
        res += (Decimal(-1)**Decimal(index+1))*(Decimal(x)**Decimal(2*index-1))/(Decimal(2)*index-1)
        index += 1
    return res

def computePi(method = 'ramanujan',k=1000):
    '''
    计算圆周率高精度值
    :param method: 计算使用的方法，默认为拉马努金公式，可以取值为:
    1:'ramanujan',每一项8位精度;2:'chudnovsky',每一项15位精度;3:'bbp':此方法可以直接算出第n位小数，而不需要提前算出前n-1位，但是收敛速度较慢
    4: 'bella':效率比'bbp'高一些;5:Machin 公式,pi = 16*arctan(1/5) - 4*arctan(1/239),每算一项得到1.4位精度
    具体参考：http://www.cnblogs.com/PegasusWang/archive/2013/03/17/2965189.html
    :param k: 计算项数
    :return:PI的值
    '''
    res = Decimal(0)
    if(method == 'ramanujan'):
        # 使用拉玛努金公式
        for i in range(k):
            res += Decimal(product(4*i))*Decimal((1103+26390*i))/(Decimal((product(i)**4))*Decimal(396**(4*i)))
        Pi = Decimal(1.)/((res*2*Decimal(2).sqrt())/Decimal(9801))
    elif(method == 'chudnovsky'):
        # 使用 chudnovsky 公式
        for i in range(k):
            res += Decimal(((-1)**i)*product(6*i)*(13591409+545140134*i))/Decimal(product(3*i)*(product(i)**3)*(640320)**(3*i+1)*Decimal(640320).sqrt())
        Pi = Decimal(1.)/(res*Decimal(12))
    elif(method == 'bbp'):
        for i in range(k):
            res += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
        Pi = res
    elif(method == 'bella'):
        for i in range(k):
            res += Decimal(1/(2**6))*Decimal(((-1)**i)/(Decimal(2)**(10*i)))*Decimal(Decimal(-2**5)/(4*i+1)-Decimal(1)/(4*i+3)+Decimal(2**8)/(10*i+1)-Decimal(2**6)/(10*i+3)-Decimal(2**2)/(10*i+5)-Decimal(2**2)/(10*i+7)+Decimal(1)/(10*i+9))
        Pi = res
    elif(method == 'machin'):
        # 注意使用 arctan 的泰勒展开
        Pi = Decimal(16)*arctan(1/5,k) - Decimal(4)*arctan(1/239,k)
    else:
        # takano 类machin 公式
        Pi = Decimal(4)*(Decimal(12)*arctan(1/49,k) + Decimal(32)*arctan(1/57,k) -Decimal(5)*arctan(1/239,k) + Decimal(12)*arctan(1/110443,k))
    return Pi

if __name__ == '__main__':
    getcontext().prec = 10000
    k = 1500
    Pi0 = computePi(k=k)
    print("Pi0(ramanujan): ",Pi0)
    Pi1 = computePi(method='chudnovsky',k=k)
    print("Pi1(chudnovsky):",Pi1)
    Pi2 = computePi(method='bbp',k=k)
    print("Pi2(bbp):       ",Pi2)
    Pi3 = computePi(method='bella',k=k)
    print("Pi3(bella):     ",Pi3)
    Pi4 = computePi(method='machin',k=k)
    print("Pi4(machin):    ",Pi4)
    Pi5 = computePi(method='takano',k=k)
    print("Pi5(takano):    ",Pi5)








