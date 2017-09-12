#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com
@File: kimmyzhang_20170912_02.py
@Time: 2017/9/12 16:00
"""

def method(NUM):
    res = ""
    remain = [2, 1]
    # 一个等号都能带来很大的影响
    # 简单的范围也很有影响
    while remain[0] > 1:
        remain = list(divmod(NUM, 2))
        if remain[1] == 0:
            res = "1" + res
            NUM = remain[0] - 1
        else:
            res = "0" + res
            NUM = remain[0]

    print(res)

method(100)
 
