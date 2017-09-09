# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-20170907-03 "

Nmk = input('输入：\n').split(' ')
for i in range(0,len(Nmk)):
    Nmk[i] = int(Nmk[i])

N = Nmk[0]
m = Nmk[1]
k = Nmk[2]

Money = input('').split(' ')
for i in range(0,len(Money)):
    Money[i] = int(Money[i])
 
index=tuple(range(0,N))

import itertools
arr = list(itertools.combinations(index, m))

mulMoney = list(1 for i in range(0,N))
for i in range(0,len(arr)):
    if max(arr[i])-min(arr[i]) <= k:
        for j in range(0,len(arr[i])):
            mulMoney[i] = mulMoney[i] * Money[arr[i][j]]

print('输出：\n%d'%(max(mulMoney)))