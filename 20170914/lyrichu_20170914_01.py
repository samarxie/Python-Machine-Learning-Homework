#!/usr/bin/env python2.7
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170914_01.py
@time: 2017/9/14 10:15
@description:
Q1:
  某餐馆有n张桌子，每张桌子有一个参数：a 可容纳的最大人数； 有m批客人，每批客人有两个参数:b人数，c预计消费金额。
在不允许拼桌的情况下，请实现一个算法选择其中一部分客人，使得总预计消费金额最大。

  输入描述:

  输入包括m+2行。 第一行两个整数n(1 <= n <= 50000),m(1 <= m <= 50000) 第二行为n个参数a,即每个桌子可容纳的最大人数,
以空格分隔,范围均在32位int范围内。接下来m行，每行两个参数b,c。分别表示第i批客人的人数和预计消费金额,以空格分隔,范
围均在32位int范围内。

  输出描述:

  输出一个整数,表示最大的总预计消费金额

  输入例子1:
  3 5
  2 4 2
  1 3
  3 5
  3 7
  5 9
  1 10
  输出例子：
  20
"""
def solveMaxConsume():
    n,m = map(lambda x:int(x),raw_input().split(" ")) # n:桌子数目 m:客人批次数目
    maxNumList = map(lambda x:int(x),raw_input().split(" ")) # 每个桌子的最大容量
    maxNumList.sort() # 桌子容量排序
    peopleNumList = [] # 每批客人人数
    consumeList = [] # 每批消费金额
    for i in range(m):
        b,c = map(lambda x:int(x),raw_input().split(" "))
        peopleNumList.append(b)
        consumeList.append(c)
    peopleConsumeList = zip(peopleNumList,consumeList) # (每批人数,消费金额) 列表
    peopleConsumeList.sort(key=lambda x:x[1],reverse=True) # 按照消费金额递减排列
    maxNum = max(maxNumList) # 所有桌子最大容量
    minPeopleNum = min(peopleNumList) # 所有批次客人最小数目
    # 如果所有桌子的最大容量的最大值都小于每个批次客人数目的最小值
    # 则无解
    maxTotalConsume = 0  # 最大消费总金额
    sitNum = 0 # 已经坐下的桌子数目
    remainPeopleNum = m # 剩下待安排的客人批次数目
    if(maxNum < minPeopleNum):
        maxTotalConsume = 0
    else:
        while(sitNum < n and remainPeopleNum > 0):
            temp = peopleConsumeList[m-remainPeopleNum]
            tempNum = temp[0]  # 该批客人人数
            tempConsume = temp[1] # 该批次的消费
            index = 0 # 选中的桌子序号
            while(index < len(maxNumList) and maxNumList[index] < tempNum):
                index += 1
            # 没有桌子能坐得下该批次的客人
            if(index == len(maxNumList)):
                remainPeopleNum -= 1
            else:
                sitNum += 1
                remainPeopleNum -= 1
                maxNumList.pop(index) # 第index个桌子已经有人，将其从列表中删除
                maxTotalConsume += tempConsume
    return maxTotalConsume


if __name__ == '__main__':
    maxTotalConsume = solveMaxConsume()
    print(maxTotalConsume)
