#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170914_02.py
@time: 2017/9/14 11:16
@description:
给定一个有n个正整数的数组A和一个整数sum,求选择数组A中部分数字和为sum的方案数。
当两种选取方案有一个数字的下标不一样,我们就认为是不同的组成方案。

  输入描述:

  输入为两行:
 第一行为两个正整数n(1 ≤ n ≤ 1000)，sum(1 ≤ sum ≤ 1000)
 第二行为n个正整数A[i](32位整数)，以空格隔开。

 输出描述：

 输出所求的方案数。

  输入例子1:
   5 15
   5 5 10 2 3
  输出例子1:
   4
"""
from copy import deepcopy
# 采用递归算法
def solve(numList,Sum):
    global total
    n = len(numList) # 数字列表长度
    if(n == 2):
        if(Sum == numList[0]):
            total += 1
        if(Sum == numList[1]):
            total += 1
        if(sum(numList) == Sum):
            total += 1
    else:
        first = numList[0] # 第一个数字
        del numList[0]
        numList_copy = deepcopy(numList)
        if(first == Sum):
            total += 1
            solve(numList_copy,Sum)
        elif(first > Sum):
            return
        else:
            numList_copy1 = deepcopy(numList_copy)
            solve(numList_copy,Sum-first)
            solve(numList_copy1,Sum)



if __name__ == '__main__':
    n,Sum = map(lambda x:int(x),raw_input().split(" "))
    numList = map(lambda x:int(x),raw_input().split(" "))
    total = 0
    numList.sort()
    solve(numList,Sum)
    print(total)

