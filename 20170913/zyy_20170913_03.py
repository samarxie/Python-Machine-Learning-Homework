# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-2017091303 顺时针打印矩阵"
"""
思路：
    1  2  3  4                         5  6  7 
    5  6  7  8   ——————————————————>   9  10 11  ————————————————————————>
    9 10 11 12   先打印第一行和第四列,  13 14 15   倒叙打印最后一行，第一列
   13 14 15 16   剩下依旧为一个矩阵                (可以将矩阵顺时针旋转180°，可循环)

   然后循环打印剩下元素组成的矩阵,直到矩阵仅剩一个元素

"""
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
import numpy as np
matrix = np.mat(matrix)

row=[]
#将需要打印的数字按顺序存如 row中

for k in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        row.append(matrix[0,j])
        if j == matrix.shape[1]-1:
            for i in range(1,matrix.shape[0]):
                row.append(matrix[i,j])
               # print(matrix[i,j])   打印后剩余元素的矩阵
    col = matrix.shape[1]                        
    matrix = matrix[1:,0:col-1]
    # 先将矩阵转置再上下置换，即是将矩阵顺时针旋转90度,转两次则180度
    matrix=matrix.T
    matrix=matrix[::-1]
    matrix=matrix.T
    matrix=matrix[::-1]
    
for i in range(len(row)):
    if i != len(row)-1:
        print(row[i],end='、')
    else:
        print(row[i])




         