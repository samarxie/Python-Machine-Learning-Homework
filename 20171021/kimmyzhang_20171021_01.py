#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171021_01.py
@Time: 2017/10/21 21:49
"""


def jump_step_by_recursion(n):
    if n == 1 or n == 2:
        return n
    else:
        return jump_step_by_recursion(n - 1) + jump_step_by_recursion(n - 2)


def jump_step_by_iteration(n):
    if n == 1 or n == 2:
        return n
    else:
        a1, a2 = 1, 2
        for _ in range(n - 2):
            a1, a2 = a2, a1 + a2
    return a2


if __name__ == '__main__':
    step_num = 100
    total_times = jump_step_by_iteration(step_num)
    print(total_times)