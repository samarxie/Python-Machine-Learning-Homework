#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171024_01.py
@Time: 2017/10/24 21:16
"""


# 用dp算法去求解，其实就是递推，不过怎么递推还是需要去思考的。
def lcs_by_dp(a, b):
    '''
    求解最大公共子序列问题
    :param a: 第一个字符串
    :param b: 第一个字符串
    :return: length of the LCS
    '''

    lena = len(a)
    lenb = len(b)
    c=[[0 for i in range(lenb+1)] for j in range(lena+1)]    # 多一位
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]

    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag


def print_lcs(flag, a, i, j):
    
    if i == 0 or j == 0:
        return
    if flag[i][j] == "ok":
        print_lcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end="")
    elif flag[i][j] == "left":
        print_lcs(flag, a, i, j - 1)
    else:
        print_lcs(flag, a, i - 1, j)


if __name__ == '__main__':
    a = 'ABCBDAB'
    b = 'BDCABA'
    c, flag = lcs_by_dp(a, b)
    for i in c:
        print(i)
    print('')
    for j in flag:
        print(j)
    print('')
    print_lcs(flag, a, len(a), len(b))
    print('')