# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-20170909-03 输出行和、列和、对角线和相等的矩阵"
"""有点暴力解,此答案不好
"""
print('输入：')
n = int(input(' '))
import numpy as np
index = [i+1 for i in range(n*n)]
np.random.shuffle(index)
arr = np.array(index).reshape(n,n)

sumNumber = int((1+n*n)*n*n/(2*3)) #各行各列对角线的和为 （1到n*n数字的和除以3）
sumArr = list(np.ones(n)*sumNumber)  
sumArr = [int(i) for i in sumArr]

k=0 
while 1 :
    sumRow=[]
    sumcol=[]
    for i in range(n):
        sumRow.append(sum(arr[i])) 
        sumcol.append(sum(arr.T[i]))
    sumMainDiag = 0 #主对角线
    for i in range(n):
        sumMainDiag = sumMainDiag + arr[i,i]
    sumCounterDiag = 0
    for i in range(n):
        sumCounterDiag = sumCounterDiag + arr[i,(n-1-i)]
    if sumMainDiag == sumNumber and sumCounterDiag == sumNumber and sumRow == sumArr and sumcol == sumArr:
        #print(arr)
        break
    index = [i+1 for i in range(n*n)]
    np.random.shuffle(index)
    arr = np.array(index).reshape(n,n)                         

print('输出：\n')
for i in range(len(arr)):
    for j in range(len(arr.T)):
        print('%d'%(arr[i,j]),end=' ')
    print('\n')
    

    
                                       

