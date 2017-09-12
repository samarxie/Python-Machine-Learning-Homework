#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/11 7:24
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170910_02.py
'''
@Description:
3 = 2+1 = 1+1+1，所以3一共有三种拆解的方式
4 = 3+1 = 2+2 = 2+1+1 = 1+1+1+1 共有5种拆法
输入一个正整数N，输出拆解的总数以及所有可能的拆解
例:
输入:3
输出:
3
3
1 2
1 1 1
'''
from copy import deepcopy
# 非递归实现版本
def decompose(n):
    if(n == 1):
        return {1:[[1]]}
    else:
        # 保存每一个数字拆解
        res_dict = {1:[[1]]}
        index = 2
        while(index <= n):
            res_list = []
            for i in range(1,index):
                for v in res_dict[index-i]:
                    v_copy = deepcopy(v)
                    v_copy.append(i)
                    res_list.append(v_copy)
            res_list.append([index])
            res_list = [sorted(v) for v in res_list]
            res_list_set = [res_list[0]]
            # 剔除重复元素
            for v in res_list[1:]:
                # 如果已经在列表中，则不添加
                if v in res_list_set:
                    continue
                else:
                    res_list_set.append(v)
            res_dict[index] = res_list_set
            index += 1
        return res_dict

# 数字分解，递归版本
# 递归版本当n非常大时，速度会显著下降
# 经过测试,n=20时，递归版本速度已经非常慢了
# 而非递归版本(循环)则不会有这个问题
def recur_decompose(n):
    if(n == 1):
        return [[1]]
    else:
        res_list = []
        for i in range(1,n):
            for v in recur_decompose(n-i):
                v_copy = deepcopy(v)
                v_copy.append(i)
                res_list.append(v_copy)
        res_list.append([n])
        res_list = [sorted(v) for v in res_list]
        res_list_set = [res_list[0]]
        # 剔除重复元素
        for v in res_list[1:]:
            # 如果已经在列表中，则不添加
            if v in res_list_set:
                continue
            else:
                res_list_set.append(v)
        return res_list_set

if __name__ == '__main__':
    n = int(raw_input())
    res_list = decompose(n)[n]
    res_list.sort(key=lambda x:len(x))
    for v in res_list:
        print(" ".join(map(lambda x:str(x),v)))
