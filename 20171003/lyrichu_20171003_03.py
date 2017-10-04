#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence
@contact: 919987476@qq.com
@software: PyCharm
@file: test10.py
@time: 2017/10/3 10:08
@description:
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。
输入描述:
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
输出描述:
对于每组数据，输出一个整数，代表最少需要删除的字符个数。
输入例子1:
abcda
google
输出例子1:
2
2
"""
import sys
while True:
    string = sys.stdin.readline().strip()
    if not string:
        break
    n = len(string)
    dp = [[0] * n for _ in range(n)]
    for i in reversed(range(n)):
        dp[i][i] = 1
        for j in range(i+1, n):
            if string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    length = dp[0][-1]
    print(n - length)
