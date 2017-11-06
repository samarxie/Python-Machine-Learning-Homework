#!/usr/bin/env python
# encoding: utf-8

"""
@author: Kimmyzhang
@license: Apache Licence 
@file: kimmyzhang_20170911_03.py
@time: 2017/9/11 17:01
"""


# 尽量不要重复代码
def get_max_index(nums):
    len_nums = len(nums)
    max_num = max(nums)
    max_index = []
    for i in range(len_nums):
        if nums[i] == max_num:
            max_index.append(i)
    left_max_index = max_index[0]
    right_max_index = max_index[-1]

    return max_num, left_max_index, right_max_index


def solution(nums):

    max_num, left_max_index, right_max_index = get_max_index(nums)
    res_list = [0 for _ in range(left_max_index)]

    # 考虑其他位置
    i = 0
    while i <= left_max_index:
        j = i + 1
        while j <= left_max_index:
            if nums[j] <= nums[i]:
                # 要对j进行加1操作
                j = j + 1
                continue
            else:
                res_list[i: j] = [nums[i] for _ in range(j - i)]
                break
        i = j

    return res_list


def solution_rain(nums):

    # 获取信息
    max_num, left_max_index, right_max_index = get_max_index(nums)
    temp1 = solution(nums)
    nums.reverse()
    temp2 = solution(nums)
    temp2.reverse()

    return temp1 +[max_num for _ in range(right_max_index - left_max_index + 1)] +temp2

if __name__ == '__main__':

    nums = [1, 2, 1, 3, 1, 4, 3, 2, 4, 3, 1, 2, 1]
    print(nums)
    print(solution_rain(nums))