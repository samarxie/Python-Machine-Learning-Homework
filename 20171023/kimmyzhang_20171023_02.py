#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171023_02.py
@Time: 2017/10/23 13:39
"""


def solution_by_dp(n, k):
    # 感觉类似于双重地推的一个关系，总是充分利用计算机的计算能力里
    # 来给出递推的式子，如果直接给出了表达式是一种情况
    # 编程的思路到底是什么呢？
    # 当while时的方法个数：

    dp = [[0] * (k + 1) for _ in range( n + 1)]

    # 基本情况
    dp[1][0] = 1

    for i in range(2, n + 1):
        for j in range(k + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] +\
                    j * dp[i - 1][j] + (i - j - 1)*dp[i - 1][j - 1]

    return dp[n][k] % 2017

if __name__ == '__main__':
    n, k = map(int, input().split(" "))
    print(solution_by_dp(n, k))
