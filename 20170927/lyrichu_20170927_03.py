#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170927_03.py
@time: 2017/9/26 16:28
@description:
python的random 模块有一个shuffle方法，其作用是将列表的所有元素随机打乱顺序然后输出。试设计一种算法，输入正整数n，将1,2,...,n 随机打乱顺序以后
输出。例如:
输入:4
输出:2,3,1,4
"""
import random

def shuffle(n):
    '''
    随机将1,2,...,n打乱以后输出(洗牌算法)
    这里采用一种简单的算法:首先从集合{1,2,...,n}随机选择一个数作为洗牌后的第一个数
    然后将其删除，接着对删除之后的集合随机取一个数作为第二个数，以此类推，直到取出所有的数
    :param n: 输入正整数
    :return: 洗牌之后的数字列表
    '''
    # 初始数字列表
    myList = list(range(1,n+1))
    # 洗牌之后的数字列表
    shuffleList = []
    while(myList):
        # 随机选择一个数字
        choose = random.choice(myList)
        # 数字位置
        index = myList.index(choose)
        shuffleList.append(choose)
        myList.pop(index)

    return shuffleList

if __name__ == '__main__':
    n = int(raw_input())
    shuffleList = shuffle(n)
    # 输出洗牌之后的数字
    print(",".join(map(lambda x:str(x),shuffleList)))

