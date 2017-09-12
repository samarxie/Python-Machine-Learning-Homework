#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/9 19:36
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170909_01.py
'''
@Description:
输入一个正整数N
输入N*N的矩阵
输出：
矩阵是否可逆，0表示不可逆，1表示可逆
输出逆矩阵
例：
输入：
2
1 0
0 1
输出：
1
1 0
0 1
'''
from copy import deepcopy
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

# 计算矩阵的逆矩阵
# 在矩阵的右边放置一个单位阵，利用行初等变换将原矩阵变为单位矩阵，则右边变换之后的矩阵即为逆矩阵
def Inv(matrix,n):
    matrix_copy = deepcopy(matrix)
    det = Det(matrix,n) # 行列式
    if(det == 0.): # 如果行列式为0
        # 矩阵不可逆
        return False,None
    else: # 矩阵可逆
        # 单位矩阵
        one_matrix = [[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                value = 1 if i==j else 0
                one_matrix[i].append(value)
        # 将matrix与 one_matrix 拼接成一个新矩阵new_matrix
        new_matrix = []
        for i in range(n):
            line1 = matrix_copy[i]
            line1.extend(one_matrix[i])
            new_matrix.append(line1)
        for i in range(n-1): # i是列
            for j in range(i,n): # j是行
                if(float(new_matrix[j][i]) == 0.):
                    continue
                else:
                    index = j
                    break

            if(index != i):
                # 交换第index行与第i行
                new_matrix[i],new_matrix[index] = new_matrix[index],new_matrix[i]
            # 利用第i行将其余各行第i列变为0
            for k in range(i+1,n):
                coef = -new_matrix[k][i]/float(new_matrix[i][i])
                # 需要到第2n列
                for t in range(i,2*n):
                    new_matrix[k][t] = new_matrix[k][t] + coef*new_matrix[i][t]
        # 行初等变换之后，new_matrix前n行，前n列组成一个上三角矩阵
        #
        for i in range(n-1):
            new_matrix[n-1-i] = [float(new_matrix[n-1-i][j])/new_matrix[n-1-i][n-1-i] for j in range(2*n)]
            for j in range(n-1-i):
                coef = -new_matrix[j][n-1-i]
                for k in range(2*n):
                    new_matrix[j][k] = new_matrix[j][k] + coef*new_matrix[n-i-1][k]
        new_matrix[0] = [float(new_matrix[0][j])/new_matrix[0][0] for j in range(2*n)]
        inv_matrix = [line[n:] for line in new_matrix]
        return True,inv_matrix

if __name__ == '__main__':
    n = int(raw_input())
    matrix = []
    for i in range(n):
        matrix.append(map(lambda x:float(x),raw_input().split(" ")))
    Bool,inv_matrix = Inv(matrix,n)
    if(Bool): # 矩阵可逆
        print("1")
        for i in range(n):
            print(" ".join(map(lambda x:str(x),inv_matrix[i])))
    else:
        # 矩阵不可逆
        print("0")
