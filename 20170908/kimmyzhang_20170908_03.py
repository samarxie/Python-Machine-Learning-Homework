#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20170908_03.py
@Time: 2017/11/6 15:50
Q3:
酒馆有m个龙头，每个龙头出酒量相等，都为1.现有n名顾客，按照顺序1...n接酒，i号顾客接酒量为w_i。
接酒开始时，1到m号顾客分别占领一个酒龙头，同时开始，并且一人接完后，下一人立刻接替。求总接酒时间？
输入：
n m
w_i
输出：
总接酒时间
样例输入：
5 3
1 2 3 4 5
样例输出：
7
"""


# 判断是否有位置进入
def get_empty_posi(nums):

    # 获得当前已经取完酒的位置
    zero_posi = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_posi.append(i)
    return zero_posi


def solution_by_simu(n, m, w_list):

    # 初始时的酒量
    posi_list = [w for w in w_list[:m]]
    # 待进入酒桶的酒量
    remain_list = [w for w in w_list[m:]]

    time = 0 # 初始时间
    while max(posi_list) != 0:
        posi_list = [num - 1 for num in posi_list]
        temp_list = get_empty_posi(posi_list)
        len_temp = len(temp_list)
        if len_temp != 0:
            for i in range(len_temp):
                posi_list[temp_list[i]] = remain_list[i]
                del remain_list[i]
                remain_list.append(0)
        time += 1

    return time


if __name__ == '__main__':
    n = 5
    m = 3
    w_list = list(range(1, n + 1))
    res = solution_by_simu(n, m, w_list)
    print(res)