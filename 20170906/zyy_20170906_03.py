# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017

@author: zyy
"""

"zyy-20170906-01 最短路程问题"
'思路'
'先计算原始应该走的距离和，再计算除去任意j点后，原始距离减去j点与j+1、j-1点距离和再加上j+1到j-1的距离'

N = int(input('点的个数N(N<=1000)\n'))
axi = []
axi = input('输入N个坐标\n').split(' ')
for i in range(0,N):
    axi[i] = int(axi[i]) 
    
distanceAll = 0 
for i in range(0,N-1):
    distanceAll +=  abs(axi[i+1]-axi[i]) 
        
dis = []

for j in range(1,len(axi)-1):
   d1 = abs(axi[j+1]-axi[j]) + abs(axi[j]-axi[j-1])
   d2 = abs(axi[j+1]-axi[j-1]) 
   distance = distanceAll - d1 + d2
   dis.append(distance)

minDistance = min(dis)
print(minDistance)


'''


print(distance)
'''