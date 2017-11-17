#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171107_02.py
@Time: 2017/11/16 16:34
Q2:
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


def solution(n):
    '''
    计算2进制中的"1"的个数
    这里，我们是用的是位运算
    :param n: 相应数字
    :return:个数
    '''
    bin_num = bin(n)
    count = 0
    while n != 0:
        count += 1
        n = n&(n - 1)

    return count


if __name__ == '__main__':
    n = 399
    print(bin(n))
    print(solution(n))