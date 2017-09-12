#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/9/7 15:47
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170907_01.py
'''
@Description:求行列式
使用高斯消元法
'''

# 计算矩阵行列式的函数
# matrix 是方阵，n是维数
def Det(matrix,n):
    sign = 1 # 交换行列式两行，行列式要变号
    for i in range(n-1): # i是列
        index = -1 # 首元素第一个非零的行数
        for j in range(i,n): # j是行
            if(float(matrix[j][i]) == 0.):
                continue
            else:
                index = j
                break
        if(index == -1): # 如果所有首元素都为0，则行列式为0
              return 0.
        else:
            if(index != i):
                # 交换第index行与第i行
                matrix[i],matrix[index] = matrix[index],matrix[i]
                sign = -sign
        # 利用第i行将其余各行第i列变为0
        for k in range(i+1,n):
            if(float(matrix[i][i]) == 0.):
                return 0.
            coef = -matrix[k][i]/float(matrix[i][i])
            for t in range(i,n):
                matrix[k][t] = matrix[k][t] + coef*matrix[i][t]
    res = 1.
    for i in range(n):
        res *= matrix[i][i]
    res *= sign
    return res

if __name__ == '__main__':
    n = int(raw_input()) # 方阵维数
    matrix = []
    for i in range(n):
        line = raw_input().split(" ")
        line = map(lambda x:float(x),line)
        matrix.append(line)
    det = Det(matrix,n)
    print("%.2f" % det)
