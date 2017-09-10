# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-20170909-01 求逆矩阵"
"思路：矩阵行列式是否为0 判断是否是可逆矩阵"
N = int(input('输入：\n'))
matrix = []
ReverMatrix=[]
for i in range(N):
    tmp = []
    tmp = input('').split(' ')
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    matrix.append(tmp)
    
import numpy as np
matrix = np.mat(matrix)
num = np.linalg.det(matrix)

if num != 0:
    ifRever = 1
    ReverMatrix = matrix.I
else:
    ifRever = 0

print('输出：\n %d' %(ifRever))
for i in range(0,len(ReverMatrix)):
    for j in range(0,len(ReverMatrix.T)):
        print('%d'%(ReverMatrix[i,j]),end=' ')
    print('\n')


    
