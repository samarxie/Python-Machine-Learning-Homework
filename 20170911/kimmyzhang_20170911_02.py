#!/usr/bin/env python
# encoding: utf-8

"""
@author: Kimmyzhang
@license: Apache Licence 
@file: kimmyzhang_20170911_02.py
@time: 2017/9/11 17:01
"""

# 将该题抽象成进制问题。即为25进制.但是要做很多准备工作。因为要处理很多特殊情况。


def getIndex(str):
    index = 0
    for i in range(4):
        if i == 0:
            index = (ord(str[i]) - 97)* pow(25, 3) + (ord(str[i]) - 96) * 3
            #print(index)

        # 这地方位置放的不同，会有什么区别
        else:
            index = index + (ord(str[i]) - 96) * pow(25, 3 - i)


    print(index-1)

getIndex("bada")
