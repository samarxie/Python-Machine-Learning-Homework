# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-20170908-01 返回最后一个最长的数字串"
"思路：用到正则表达式"

string = input('输入：\n')

import re
number = []
number = re.findall(r'\d+', string) #直接查找字符串中包含的数字串

length=[None]*len(number)
for i in range(0,len(number)):
    length[i] = len(number[i])

print('输出：')
for i in range(0,len(number)):
    if length[i] == max(length):
        print(number[i])
        print(max(length))  
