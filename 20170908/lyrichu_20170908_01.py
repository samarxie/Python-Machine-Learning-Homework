#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/8 13:52
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170908_01.py
'''
@Description:
在一个字符串中找出长度最长的数字串，并返回最后一个最长的数字串及其长度
样例：
输入：
abcd12345ed125ss123058789
输出：
123058789
9
'''
def getSubStrList(string):
    numbers = [str(i) for i in range(10)] # 数字字符数组
    subStrList = [] # 数字串列表
    index = 0 # 记录指向字符的位置
    while(index < len(string)):
        if string[index] in numbers:
            subStr = string[index]
            index += 1
            while(index < len(string) and string[index] in numbers):
                subStr += string[index]
                index += 1
            subStrList.append(subStr)
        else:
            index += 1
    return subStrList
if __name__ == '__main__':
    string = raw_input() # 输入字符串
    subStrList = getSubStrList(string)
    subStrLenList = [len(subStr) for subStr in subStrList]
    maxLen = max(subStrLenList) # 最大字符串长度
    # 输出最长数字子串的最后一个
    maxLenLastStr = [subStr for subStr in subStrList if len(subStr) == maxLen][-1]
    print(maxLenLastStr)
    print(maxLen)
