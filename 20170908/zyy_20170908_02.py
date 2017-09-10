# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""
"zyy-2017090802 100人围圈"
"""
思路: 报数1 2 3 时候 可以转变为100人按顺序排3列。
      1  2  3                 1  2              10  11  1
      4  5  6    ——————————>  4  5  ——————————> 2   4   5   
      7  8  9    删掉第三列   7  8     重新排    7   8
      10 11                  10 11                  |
         |                                          |
         |         <——————    循环    <——————       |
      
      删掉第三列，并将最后不足3个的行放置前面，
      形成一维数组再重新按顺序排成3列的方阵，
      重复该循环，直到队伍剩下不足三人
"""

M = int(input('样例输入：\n'))
N = 100  
numberlist= list(range(1,N+1))

import numpy as np
while len(numberlist) >= M:
    row  =  int(len(numberlist)/M)
    l = int(len(numberlist) % M)
    num = numberlist
    arr = np.array(numberlist[0:row*M]).reshape(row,M) #将一员数组转化为行数为row，列数为M的矩阵
    arr = np.delete(arr,[M-1],axis=1)  #删掉矩阵中第M列
    numberlist = arr.flatten()  #将矩阵转化为一元数组
    if l != 0:
        for i in range(0,l)[::-1]: #倒叙遍历
            numberlist= list(numberlist)
            numberlist.insert(0,num[len(num)-l+i])
    #print(numberlist)  可以将过程打印出来

numberlist = sorted(numberlist)
for i in range(len(numberlist)):
    print(numberlist[i],end=' ')

















