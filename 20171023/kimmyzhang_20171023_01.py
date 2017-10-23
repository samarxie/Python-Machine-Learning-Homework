#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171023_01.py
@Time: 2017/10/23 13:39
"""

# 当数字过大时会出现什么情况


def solution(a_list):
    list_len = len(a_list)
    count_list = [0] * 10
    for i in range(list_len):
        count_list[a_list[i]] += 1
    return print(count_list)


if __name__ == '__main__':
    test_list = list(map(int, input().split(" ")))
    solution(test_list)

