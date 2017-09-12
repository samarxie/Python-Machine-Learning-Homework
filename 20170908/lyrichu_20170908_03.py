#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/9/8 18:38
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170908_03.py
'''
@Description:
3、酒馆有m个龙头，每个龙头出酒量相等，都为1.现有n名顾客，按照顺序1...n接酒，i号顾客接酒量为w_i。接酒开始时，1到m号顾客分别占领一个酒龙头，同时开始，并且一人接完后，下一人立刻接替。求总接酒时间？
输入：
n m
w_i
输出：
总接酒时间
样例输入：
5 3
1 2 3 4 5
样例输出：
7
'''
n,m = map(lambda x:int(x),raw_input().split(" "))
w = map(lambda x:int(x),raw_input().split(" "))
indexWineState = [[i,0,0] for i in range(1,n+1)] # [序号,酒量,时间] 初始化列表
waitList = [[i,0,0] for i in range(1,n+1)] # 等待列表
getWineList = list(range(1,m+1)) # 当前接酒人列表
while(waitList != [] or len(getWineList) != 0):
    if len(waitList) >= m:
        getWineList = [v[0] for v in waitList[0:m]] # 接酒人序号
        del waitList[0:m]
    else:
        getWineList = [v[0] for v in waitList]
        waitList = []
    if(getWineList != []):
        for waitPer in waitList:
            indexWineState[waitPer[0]-1][2] += 1 # 等待人时间+1
    for perIndex in getWineList:
        indexWineState[perIndex-1][1] += 1 # 接酒加1
        indexWineState[perIndex-1][2] += 1 # 时间加1
        if(indexWineState[perIndex-1][1] < w[perIndex-1]): # 如果没有接满
            waitList.append(indexWineState[perIndex-1]) # 加入等待列表

print(max([v[2] for v in indexWineState])) # 输出最长时间
