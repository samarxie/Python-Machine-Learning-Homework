#!/usr/bin/env python
# encoding: utf-8

"""
@author: Kimmyzhang
@license: Apache Licence 
@file: kimmyzhang_20170911_01.py
@time: 2017/9/11 16:41
"""

def geohashCode(N):
    # 分析时不需要分类讨论正负的问题
    result = ""
    upper, low = 90, -90
    iteration_time = 0
    precision_num = 6
    while iteration_time < precision_num:
        interval = int((upper + low)/2)
        if N >= interval:
            low = interval
            result += "1"
        else:
            upper = interval
            result += "0"
        iteration_time += 1
    print(result)



if __name__ == '__main__':
    N = int(input("请输入纬度： "))
    geohashCode(N)
