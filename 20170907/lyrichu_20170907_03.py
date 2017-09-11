#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/7 19:51
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170907_03.py
'''
@Description:计算最大乘积
'''
from itertools import combinations
# 计算列表所有元素乘积
def product(mylist):
    res = 1
    for i in mylist:
        res *= i
    return res

n,m,k = map(lambda x:int(x),raw_input().split(" ")) # 学生人数
power_list = map(lambda x:int(x),raw_input().split(" ")) # 钱数列表
product_list = [] # 钱数乘积列表
power_comb_list = list(combinations(range(n),m))
for power_comb in power_comb_list:
    power_comb = list(power_comb)
    power_comb.sort()
    flag = True
    for i in range(m-1):
        if(power_comb[i+1]-power_comb[i] > k):
            flag = False
            break
        else:
            continue
    if(flag):
        product_list.append(product([power_list[i] for i in power_comb]))
print(max(product_list))
