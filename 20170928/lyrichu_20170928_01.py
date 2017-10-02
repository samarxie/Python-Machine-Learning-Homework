#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170928_01.py
@time: 2017/9/28 10:49
@description:使用python求解八皇后问题。
"""
import random

def conflict(solveList,nowPos):
    '''
    判断当前位置和之前皇后的位置是否冲突
    :param nowPos: 当前皇后摆放位置
    :param solveList: 之前已经摆好的皇后位置
    :return: 当前位置和之前皇后的位置是否冲突，True表示冲突，False表示不冲突
    '''
    # flag 表示是否冲突
    flag = False
    # 如果solveList为空
    if(not solveList):
        return flag
    else:
        # 判断列以及对角线是否冲突
        for queen in solveList:
            # 如果在同一列或者是在同一条对角线上
            if(nowPos[1] == queen[1] or (abs(queen[0]-nowPos[0]) == abs(queen[1]-nowPos[1]))):
                flag = True
                return flag
            else:
                continue
    return flag


def eightQueens(n = 8):
    '''
    求解八皇后问题
    :param n: 问题规模
    :return: 某一个可能的解,每一个解是一个列表,列表的元素为元组(i,j)表示皇后在第i行第j列上
    '''
    # 初始化解集合
    solveList = []
    # 遍历每一行
    # 初始化行数,列数
    row = 1
    # 第一行皇后列的位置
    col = 1
    # index 记录第一行列的变化
    while(row <= n):
        nowPos = (row,col)
        while(nowPos[1] <= n and conflict(solveList,nowPos)):
            nowPos = (nowPos[0],nowPos[1]+1)
        if(nowPos[1] == n+1):
            row = 1
            # 随机选取一列
            col = random.randrange(1,n+1)
            solveList = []
        else:
            solveList.append(nowPos)
            row += 1
            # 随机选取一列作为下一行的开始列
            col = random.randrange(1,n+1)
    return solveList

def prettyPrint(solveList):
    '''
    将结果直观打印出来
    用 x 表示皇后，其余地方用*表示
    :param solveList: 一个可行解
    :return: None
    '''
    # 皇后个数
    n = len(solveList)
    for i in range(n):
        printRow = ''
        for j in range(n):
            printChar = 'x ' if solveList[i][1] == j+1 else '* '
            printRow += printChar
        print(printRow)


if __name__ == '__main__':
    solveList = eightQueens()
    print(solveList)
    prettyPrint(solveList)





