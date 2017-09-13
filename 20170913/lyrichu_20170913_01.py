#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/13 9:05
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170913_01.py
'''
@Description:
Q1：
  在字符串中寻找出，第一个只出现一次的字符。
 举例：
   "abaccdeff"，则输出"b"。
'''
string = raw_input()
n = len(string) # 字符串长度
flag = False  # 是否有只出现一次的字符
ch = ''
for i in range(n):
    count = 0 # 记录每个字符出现次数
    ch = string[i]
    for j in range(n):
        if(ch == string[j]):
            count += 1
    if(count == 1):
        flag = True
        break

if(flag):
    print(ch)
else:
    print(0)






