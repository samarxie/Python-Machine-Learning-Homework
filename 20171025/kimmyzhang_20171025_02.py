#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171025_02.py
@Time: 2017/10/25 10:40
"""


import random


def merge_sort(a):
    '''
    merge sort
    :param a: a list to be sorted
    :return: a sorted list
    '''
    len_list = len(a)
    middle = round(len_list / 2)
    left_list = a[0:middle]
    right_list = a[middle + 1:-1]
    res_list = []

    while True:
        middle = round(len(left_list))
        left_list = left_list[0: middle]
        right_list = right_list[middle + 1: -1]
        print([left_list] + [right_list])




    return res_list


def partion(list):

    # 特殊情况处理
    if len(list) <= 1:
        return list

    # middle
    mid = round(len(list) / 2)
    print(mid)

    # 这个地方进行递归, 如何进行切分, 精华所在
    left_list = partion(list[:mid])
    right_list = partion(list[:-1])
    res = []

    # 将切分数组分别进行比较，并将数字天道res_List后面
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] <= right_list[0]:
            res.append(left_list.pop(0))
        else:
            res.append(right_list.pop(0))

    # 当出现了某个切片数组的长度为0的时候，直接把另一个数组给加上去。
    # 要注意，我们是用数组的长度作为判断依据的
    if len(left_list) > 0:
        res.extend(partion(left_list))
    else:
        res.extend(partion(right_list))

    return res

def ConfiationAlgorithm(str):
    if len(str) <= 1: #子序列
        return str
    mid = (len(str) / 2)
    left = ConfiationAlgorithm(str[:mid])#递归的切片操作
    right = ConfiationAlgorithm(str[mid:len(str)])
    result = []
    #i,j = 0,0

    while len(left) > 0 and len(right) > 0:
        if (left[0] <= right[0]):
            #result.append(left[0])
            result.append(left.pop(0))
            #i+= 1
        else:
            #result.append(right[0])
            result.append(right.pop(0))
            #j+= 1

    if (len(left) > 0):
        result.extend(ConfiationAlgorithm(left))
    else:
        result.extend(ConfiationAlgorithm(right))
    return result


if __name__ == '__main__':
    a = [random.randint(1, 100) for _ in range(10)]
    print(a)
    # partion(a)
    ConfiationAlgorithm(a)