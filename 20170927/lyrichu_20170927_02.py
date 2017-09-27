#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170927_02.py
@time: 2017/9/26 16:28
@description:
给定一个正整数n，集合{1,2,...,n}的所有子集(包括空集)显然有2^n个，请按照字典顺序逐个输出这2^n个子集。
例:
输入:3
输出:
{}
{1}
{1,2}
{1,2,3}
{1,3}
{2}
{2,3}
{3}
"""

def generateSubset(n):
    '''
    产生1,2,...,n的所有子集
    :param n:正整数n
    :return:所有子集列表
    '''
    # 初始化子集列表
    subSetList = ['{}']
    for i in range(2**n-1):
        if(i == 0):
            subSetList.append('1')
        else:
            # 取出上一次最后一个元素作为当前元素
            now = subSetList[-1]
            # 当前元素的末尾数字
            endNum = int(now[-1])
            # 末尾数字没有达到最大
            if(endNum < n):
                # 下一个增加的字符
                nextChar = str(endNum + 1)
                # 下一个元素
                new = now + nextChar
                subSetList.append(new)
            # 末尾数字已经达到最大
            else:
                #删除最后一个字符
                now = now[:-1]
                # 末尾数字加1
                # 得到新的元素
                new = now[:-1] + str(int(now[-1])+1)
                subSetList.append(new)
    # 为元素添加大括号和逗号
    for i in range(1,2**n):
        element = subSetList[i]
        new = "{" + ",".join(element) + "}"
        subSetList[i] = new

    return subSetList


if __name__ == '__main__':
    n = int(raw_input())
    subSetList = generateSubset(n)
    for subset in subSetList:
        print(subset)





