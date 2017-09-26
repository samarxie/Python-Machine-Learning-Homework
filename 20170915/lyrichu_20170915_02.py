#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170915_02.py
@time: 2017/9/25 21:11
@description:了解字符串的朴素匹配与KMP匹配算法。并使用python实现
"""

def simpleMatch(matchStr,sourceStr):
    '''
    :param matchStr: 待匹配的字符串
    :param sourceStr: 源字符串
    :return: 第一次匹配到字符串的index，如果没有匹配到则返回-1
    '''
    # 初始化index
    index = 0
    # 源字符串长度
    sourceStrLen = len(sourceStr)
    # 匹配字符串长度
    matchStrLen = len(matchStr)
    while(index < sourceStrLen):
        # 初始化匹配字符串的位置
        pos = 0
        while(pos < matchStrLen and matchStr[pos] == sourceStr[index]):
            pos += 1
            index += 1
        if(pos == matchStrLen):
            return index - matchStrLen
        else:
            index += 1
            continue
    return -1

def calNext(matchStr):
    '''
    计算next数组
    :param matchStr: 待匹配的字符串
    :return: next数组
    '''
    Next = []
    # 源字符串长度
    matchStrLen = len(matchStr)
    # 逐个计算next数组的值
    for i in range(matchStrLen):
        if(i == 0):
            Next.append(0)
        else:
            index = i
            while(index >= 0):
                if(matchStr[0:index] == matchStr[(i+1-index):i+1]):
                    Next.append(index)
                    break
                else:
                    index -= 1
            if(index == -1):
                Next.append(0)
    return Next

def kmpMatch(matchStr,sourceStr):
    '''
    :param matchStr: 待匹配的字符串
    :param sourceStr: 源字符串
    :return: 第一次匹配到字符串的index，如果没有匹配到则返回-1
    '''
    # 计算Next数组
    Next = calNext(matchStr)
    # 初始化index
    index = 0
    # 源字符串长度
    sourceStrLen = len(sourceStr)
    # 匹配字符串长度
    matchStrLen = len(matchStr)
    while(index < sourceStrLen):
        # 初始化匹配字符串的位置
        pos = 0
        while(pos < matchStrLen and matchStr[pos] == sourceStr[index]):
            pos += 1
            index += 1
        if(pos == matchStrLen):
            return index - matchStrLen
        else:
            index += (Next[pos]+1)
            continue
    return -1


if __name__ == '__main__':
    matchStr = 'bda'
    sourceStr = 'sjdabcabdabdf'
    # 首先使用sinpleMatch
    simpleIndex = simpleMatch(matchStr,sourceStr)
    print("simpleMatch:index=%d" % simpleIndex)
    # 使用 KMP 匹配
    kmpIndex = kmpMatch(matchStr,sourceStr)
    print("kmpMatch:index=%d" % kmpIndex)





