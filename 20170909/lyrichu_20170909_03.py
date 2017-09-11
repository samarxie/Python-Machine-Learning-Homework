#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/9 21:31
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170909_03.py
'''
@Description:
Q3:
设n为奇数，将1到n*n这个n*n个数字排列成为一个n*n的方阵，使得各行，各列以及对角线上的数字之和相等。
输入:
n
输出:
满足条件的n*n的方阵(不唯一,任意输出一个满足条件的)
例:
输入:
3
输出:
2 9 4
7 5 3
6 1 8
'''

# 这里求幻方的方法为拉-卢贝尔算法
# 具体参见:http://www.cnblogs.com/Open_Source/archive/2013/02/22/2922031.html

def magic(n):
    """
    :param n: n为一个奇数,为幻方的阶数
    :return: 返回n阶幻方
    """
    matrix = [[0 for i in range(n)] for j in range(n)] # 初始化幻方
    value = 1 # value 为下一个填入幻方的值
    position = [0,(n+1)/2 - 1] # 当前的位置
    matrix[position[0]][position[1]] = value
    while(value < n*n):
        rightUpPos = [position[0]-1,position[1]+1] # 右上角坐标，行减1，列加1
        if(position == [0,n-1]): # 如果当前位于最右上角
            position = [1,n-1] # 下一个位置坐标
        else:
            if(rightUpPos[0] < 0): # 右上角横坐标小于0
                position = [n-1,rightUpPos[1]] # 纵坐标不变，横坐标变为n-1
            elif(rightUpPos[1] > n-1): # 右上角纵坐标大于n-1
                position = [rightUpPos[0],0] # 横坐标不变,纵坐标变为0
            elif(matrix[rightUpPos[0]][rightUpPos[1]] > 0): # 右上角已经有值
                if(position[0] < n-1):
                    position[0] += 1 # 将下一个数字放在当前数字下方
                else:
                    position[0] = 0
            else:
                position = rightUpPos
        value += 1
        matrix[position[0]][position[1]] = value
    return matrix

if __name__ == '__main__':
    n = int(raw_input())
    matrix = magic(n)
    for i in range(n):
        print(" ".join(map(lambda x:str(x),matrix[i])))
