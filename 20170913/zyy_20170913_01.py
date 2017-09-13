# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:24:19 2017
python 3.5
@author: zyy
"""

"zyy-2017091303 字符串中寻找第一个只出现一次的字符"
"""
思路：遍历，某字符串包含该子字符串的个数为1，则该字符只出现一次
"""

string = "abaccdeff"

for i in range(0,len(string)):
    count = string.count(string[i])
    if count == 1:
        print(string[i])
        break
