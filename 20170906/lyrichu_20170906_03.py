#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/9/6 8:53
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170906_03.py
'''
@Description:求最短路程
'''
num = int(raw_input()) # 输入点的数量
points_list = raw_input().split(" ")
points_list = [int(point) for point in points_list] # 点列表
all_distance = 0
# 计算所有相邻点总距离
for i in range(num-1):
    all_distance += abs(points_list[i] - points_list[i+1])
distance_list = [] # 存放所有可能路程列表
for i in range(1,num-1):
    distance = all_distance - abs(points_list[i-1]-points_list[i]) - abs(points_list[i+1]-points_list[i]) + abs(points_list[i-1]-points_list[i+1])
    distance_list.append(distance)
print(min(distance_list))  # 输出最短路程
