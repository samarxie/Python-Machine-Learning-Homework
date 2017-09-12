#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/12 22:18
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170912_03.py
'''
@Description:
Q3:给定一串字符串,规定连续出现m次的字符串为部分字符串,例如"aabbcdd"的部分字符串有"aa","bb","c","dd"，求任意给定字符串的所有
部分字符串的平均长度。
输入:任意字符串
输出:所有部分字符串的平均长度
例:
输入:aabbcdd
输出:1.75
'''
string = raw_input()
length = len(string)
sub_string_list = []
index = 0
while(index <length):
    sub_string = string[index]
    while(index < length -1 and string[index+1] == string[index]):
        sub_string += string[index+1]
        index += 1
    sub_string_list.append(sub_string)
    index += 1

print("%.2f" % (length/float(len(sub_string_list))))
