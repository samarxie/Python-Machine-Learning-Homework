#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20170913_02.py
@Time: 2017/9/14 18:54
"""

def is_ugly(N):
    while N % 2 == 0:
        if N == 2:
            return True
        N = int(N / 2)

    while N % 5 == 0:
        if N == 5:
            return True
        N = int(N /5)

    while N % 3 == 0:
        if N == 3:
            return True
        N = int(N / 3)


    if N not in [2, 3, 5]:
        return False

# print(is_ugly(3))

def out_ugly_number(N):
    index = 1
    number = 2
    out_list = [1]
    while index < N:
        if is_ugly(number):
            index += 1
            out_list = out_list + [number]
        number += 1
    print(out_list)

out_ugly_number(15)
