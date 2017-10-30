#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171030_01.py
@Time: 2017/10/30 11:36
Q1:
一个只包含'A'、'B'和'C'的字符串，如果存在某一段长度为3的连续子串中恰好'A'、'B'和'C'各有一个，那么这个字符串就是纯净的，否则这个字符串就是暗黑的。例如：
BAACAACCBAAA 连续子串"CBA"中包含了'A','B','C'各一个，所以是纯净的字符串
AABBCCAABB 不存在一个长度为3的连续子串包含'A','B','C',所以是暗黑的字符串
你的任务就是计算出长度为n的字符串(只包含'A'、'B'和'C')，有多少个是暗黑的字符串。
输入一个整数n，表示字符串长度(1 ≤ n ≤ 30)
输出一个整数表示有多少个暗黑字符串
"""


def count_black_str_dp(n):

    # 思考和动态规划的区别

    if  n == 1:
        return 3
    elif n == 2:
        return 9
    else:
        record_list = [3, 9]
        for i in range(2, n):
            black_str = 2 * record_list[i - 1] + record_list[i - 2]
            record_list.append(black_str)

        return record_list[n - 1]


if __name__ == '__main__':
    n = 10
    print(count_black_str_dp(n))
