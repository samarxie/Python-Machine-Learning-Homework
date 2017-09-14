#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170914_03.py
@time: 2017/9/14 15:00
@description:
C市现在要转移一批罪犯到D市，C市有n名罪犯，按照入狱时间有顺序，另外每个罪犯有一个罪行值，值越大罪越重。
现在为了方便管理，市长决定转移入狱时间连续的c名犯人，同时要求转移犯人的罪行值之和不超过t，问有多少种选择的方式？

 输入描述:

  第一行数据三个整数:n，t，c(1≤n≤2e5,0≤t≤1e9,1≤c≤n)，第二行按入狱时间给出每个犯人的罪行值ai(0≤ai≤1e9)


  输出描述:

  一行输出答案。

  输入例子1:

   3 100 2
   1 2 3


  输出例子1:

  2
"""
def solve():
    n,t,c = map(lambda x:int(x),raw_input().split(" ")) # n:罪犯数目,t:罪行之和不超过t,c:连续c名犯人
    aList = map(lambda x:int(x),raw_input().split(" ")) # 每个犯人罪行值列表
    choice = 0 # 总选择数目
    for i in range(n-c+1):
        if(sum(aList[i:i+c]) <= t):
            choice += 1
    return choice

if __name__ == '__main__':
    choice = solve()
    print(choice)
