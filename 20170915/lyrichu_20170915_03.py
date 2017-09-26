#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170915_03.py
@time: 2017/9/25 21:11
@description:基本的快速排序算法
"""
from __future__ import print_function
import random

def quickSort(L, low, high):
    '''
    :param L: 待排序的列表
    :param low: 左标记
    :param high: 右标记
    :return: 完成排序之后的列表
    '''
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

if __name__ == '__main__':
    # 0-99 的顺序列表
    L = list(range(100))
    # 将列表随机打乱
    random.shuffle(L)
    print("before sort:",L)
    quickSort(L,0,99)
    print("after quick sort:",L)
