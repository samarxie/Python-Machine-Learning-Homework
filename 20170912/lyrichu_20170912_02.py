#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/12 22:16
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170912_02.py
'''
@Description:
Q2:小明手里有一些钱，现在有两个聚宝盆编号为0号和1号。0号的特性是:如果给它投入x的钱，它会变出2*x+1的钱；1号的特性是：
如果给它投入x的钱，它会变出2*x+2的钱。(这里x可以为0)。现在小明手里没有钱，如果他想得到n数量的钱，应该按照什么样的顺序使用
两个聚宝盆呢？
输入:n
输出:
依次使用聚宝盆的序号。
例如:
输入: 10
输出: 0 1 1(表示依次使用0号，1号，1号聚宝盆)
'''
n = int(raw_input())
str_list = [] # 记录每次选择的机器
while(n >= 1):
    # 如果n是偶数
    if(n % 2 == 0):
        str_list.append('1') # 选择第二个机器
        n = (n-2)/2
    else:
        str_list.append('0')
        n = (n-1)/2
# 选择机器之前是从后往前选的，所以需要reverse一下
str_list.reverse()
print("".join(str_list))
