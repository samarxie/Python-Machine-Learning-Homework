#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/8 17:55
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170908_02.py
'''
@Description:
2、100个人围成一圈，编号从1开始到100.从1开始报数，报到M的人自动退出，下一个人接着从1开始报数，直到剩余人数小于M。求最后剩余人的编号。
样例输入：
3
样例输出：
58 91
样例输入2：
4
样例输出2：
34 45 97
'''
m = int(raw_input())
restNum = 100 # 剩余人数
indexNumberList = [[i,(i-1)%m + 1] for i in range(1,restNum+1)] # [学生序号,列表] 组成的列表
lastNumber = m if restNum % m == 0 else restNum % m # 最后一个学生的报数
while(restNum >= m):
    indexNumberList = [v for v in indexNumberList if v[1] != m] # 删除报数为 m的学生
    indexNumberList[0][1] = 1 if lastNumber+1>m else lastNumber+1 # 学生报数m之后，下一个为1
    restNum = len(indexNumberList) # 更新剩余人数
    # 逐个报数
    for i in range(restNum-1):
        indexNumberList[i+1][1] = indexNumberList[i][1] + 1
        if(indexNumberList[i+1][1] > m):
            indexNumberList[i+1][1] = 1
    lastNumber = indexNumberList[-1][1] # 记录最后一个人的报数

print(" ".join(map(lambda x:str(x),[v[0] for v in indexNumberList])))
