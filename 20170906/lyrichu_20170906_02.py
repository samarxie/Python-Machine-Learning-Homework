#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/9/6 8:45
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170906_02.py
'''
@Description:输出前N个斐波那契数列
'''
num = int(raw_input()) # 输入N
f_list = [] # 存放数字的数组
for i in range(num):
    if i == 0 or i == 1:
        f_list.append(i)
    else:
        f_list.append(f_list[i-1] + f_list[i-2])
print(" ".join([str(i) for i in f_list]))
