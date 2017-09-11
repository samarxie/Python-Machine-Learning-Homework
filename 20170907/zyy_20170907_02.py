# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-20170907-01 从该集合中选取n个数的所有可能"
"""
思路：递归实现
一个数组 data 有 n 个元素，从中选取 m 个数的组合 arr
1） 选择 data的第1个元素为arr的第一个元素，即：arr[0] = data[0]； 
2） 在data第一个元素之后的其它元素中，选取其余的 m - 1个数，这是一个上述问题的子问题，递归即可。 
3） 依次选择 data的第 2 到 n - m + 1元素作为起始点，再执行1、2步骤。 
4） 递归算法过程中的 m = 0 时，输出 arr 的所有元素。
itertools包中combinations可以实现
"""
nm = []
array = []
nm = input('输入：\n').split(' ')

array = input('').split(' ')
for i in range(0,len(nm)):
    nm[i] = int(nm[i]) 
    
n = nm[0]
m = nm[1]  

for i in range(0,len(array)):
    array[i] = int(array[i]) 

array = tuple(array)
arr = []
import itertools 
arr = list(itertools.combinations(array, m))

for i in range(len(arr)):
    print('%d %d' % arr[i])

  
        
