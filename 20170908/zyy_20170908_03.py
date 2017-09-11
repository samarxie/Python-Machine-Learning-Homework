# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-2017090803 酒馆接水"
"""
思路：
 前面三个人先接酒 (1) 1 2 3   —— 1 分钟后（min（1 2 3） 
 第四个人开始接   (2) 4 1 2   —— 1 分钟后
 第五个人开始接   (3) 3 5 1   —— 5 分钟后，最后一个人才接完，一共用7分钟
 """
nm = input('样例输入：\n').split(' ')
n = int(nm[0])
m = int(nm[1])

w_i = input('').split(' ')
for i in range(len(w_i)):
    w_i[i] = int(w_i[i])

f=[]
for i in range(m):
    f.append(w_i[i])

process =[]
Min = 0
for i in range(m,len(w_i)):
    Min = Min + min(f)
    a = f.index(min(f)) 
    print(a)
    f = [x-min(f) for x in f]
    f[a] = w_i[i]
    process.append(f)
Min = Min + max(f)
print("样例输出：")
print(Min)
"""可以打印过程
print(process)

"""





