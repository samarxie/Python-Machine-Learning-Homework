#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171030_02.py
@Time: 2017/10/30 11:36
Q2:
给定一个有n个正整数的数组A和一个整数sum,求选择数组A中部分数字和为sum的方案数。
当两种选取方案有一个数字的下标不一样,我们就认为是不同的组成方案。
输入为两行:
第一行为两个正整数n(1 ≤ n ≤ 1000)，sum(1 ≤ sum ≤ 1000)
第二行为n个正整数A[i](32位整数)，以空格隔开。
输出所求的方案数
"""


import numpy as np


def solution(nums, n, sum):
    sum_arr = [[0] * (sum + 1) for _ in range(n + 1)]
    # sum_arr[i][0] = 1,即 i个数字组成和为0只有一种方案，就是什么都不取
    for i in range(n + 1):
        sum_arr[i][0] = 1
    for i in range(1, n + 1):
        for j in range(sum + 1):
            # 如果第i个数字nums[i-1]小于等于和j,则分为包括第i个数字和不包括第i个数字两种情况
            # sum_arr[i-1][j] 表示前i-1个数字组成和为j的方案数目
            # sum_arr[i-1][j-nums[i-1]] 表示 包括 第i个数字nums[i-1]在内，前i-1个数字和为j-nums[i-1](这样i个数字的和刚好为j)
            if (nums[i - 1] <= j):
                sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i - 1][j - nums[i - 1]]
            else:
                # 如果第i个数字nums[i] 大于和j
                # 则只需要考虑前i-1个数字组成和为j的情况了
                sum_arr[i][j] = sum_arr[i - 1][j]

    return sum_arr[n][sum]


if __name__ == '__main__':
    n, sum = 10, 5
    nums = [np.random.randint(1, 10) for _ in range(n)]
    print(solution(nums, n, sum))