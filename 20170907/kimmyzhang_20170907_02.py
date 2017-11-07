#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20170907_02.py
@Time: 2017/11/2 15:24
Q2:
输入两个正整数m,n(m>=n)
输入一个含有m个不同正整数的集合
输出从该集合中选取n个数的所有可能(不计顺序)
"""


# 顺着组合数的形成方式，给出组合数
def col_num_dp(n, r):
    '''
    组合数递推公式
    :param n:
    :param r:
    :return: 组合数递推公式
    '''

    # 注意到这里的复制应当用列表表达式
    dp_list = [list(range(1, n+1)) for _ in range(r)]

    for row in range(1, r):
        for col in range(1, n):
            # 注意生成一个合适的数组
            if row == col:
                dp_list[row][col] = 1
            else:
                # 要注意列表范围
                dp_list[row][col] = dp_list[row][col - 1] + dp_list[row - 1][col - 1]

    return dp_list[r - 1][n - 1]


def is_ending(nums, m):
    for i in range(m):
        if nums[i] != 0:
            return False
    return True


# 改变数组是核心代码，要仔细考虑清楚
def change(nums):
    '''

    :param nums:传入数组
    :return: 改变后的数组
    '''

    # print(nums)
    len_nums = len(nums)
    for i in range(len_nums - 1):
        # 最后一个保证不越界
        if nums[i] == 1 and nums[i + 1] == 0:
            # 交换元素
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # 获得第一个“10”所在的指标位置
            index = i
            break

    # 把index左边的数字全部怼到最左边
    # 1.首先截取左边的数字
    left_list = nums[:index]
    # print(left_list)
    right_list = nums[index:]
    # print(right_list)
    if len(left_list) == 0:
        return right_list
    else:
        for i in range(index):
            if left_list[i] == 1:
                # index2 = i
                break
        # print(index)
        # print(index2)
        # print(left_list[index2:])
        # print(right_list)
        return left_list[i:] + [0 for _ in range(i)] + right_list


def solution_by_math(m, n):
    # 指标数组
    index_list = [1 for _ in range(m)] + [0 for _ in range(n - m )]
    print(index_list)
    # print(index_list)
    # 指标放在第一位，当index处于m-n位置时，结束
    while not is_ending(index_list, m):
        index_list = change(index_list)
        print(index_list)


def solution_by_rec(m, n):
    return True


if __name__ == '__main__':
    m = 3
    n = 5

    # res = change([1, 1, 0, 0, 1])
    # print(res)
    solution_by_math(m, n)