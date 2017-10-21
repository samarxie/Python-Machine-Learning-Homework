#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171021_02.py
@Time: 2017/10/21 21:52
"""


# 用递归的方法做的
def solution(n):
    if n == 1 or n == 2:
        return n
    else:
        res = 0
        while n > 1:
            res = res + solution(n - 1)
            n = n - 1
    # 自己到自己还有一种
    return res + 1

if __name__ == '__main__':
    step_num = 10
    res = solution(step_num)
    print(res)