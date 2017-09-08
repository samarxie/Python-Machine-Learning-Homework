# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-20170907-01 输出该矩阵的行列式"
"输入矩阵的思路：创建一个列表tuple，tuple中每一个元素也是一个列表"
"首先，我们先构造每一个元素temp列表,然后，将每个元素temp列表（append）进matric中去"

N = int(input('输入：\n'))
matrix = []
for i in range(N):
    tmp = []
    tmp = input('').split(' ')
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
    matrix.append(tmp)

"numpy 可用于矩阵运算"
import numpy as np
matrix = np.array(matrix)
num = np.linalg.det(matrix)
print('输出：\n%.2f' % num)

