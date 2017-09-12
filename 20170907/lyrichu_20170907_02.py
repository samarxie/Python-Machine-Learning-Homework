#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/9/6 22:56
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : combinations.py
'''
@Description:计算组合数
参考思路:http://blog.csdn.net/todototry/article/details/1403807
'''
from copy import deepcopy
# 从mylists m个数当中选取n个数
# 返回所有可能的组合(二维列表)
def combinations(mylists,m,n):
    res_index_list = []
    index_list = [1 for i in range(n)]
    index_list.extend([0 for i in range(m-n)])
    index_list_copy = deepcopy(index_list) # 注意需要深复制，否则只是将引用赋值
    res_index_list.append(index_list_copy)
    while(index_list[m-n:] != [1 for i in range(n)]):
        index = 0
        while(index_list[index:index+2]!= [1,0]): # 找到第一次出现1 0的位置
            index += 1
        index_list[index],index_list[index+1] = index_list[index+1],index_list[index] # 交换0和1的值
        if(index_list[0] == 0):
            temp = index_list[:index]
            temp.reverse()
            temp.extend(index_list[index:])
            index_list = temp
        index_list_copy = deepcopy(index_list)
        res_index_list.append(index_list_copy)
    res_list = []
    for v in res_index_list:
        temp_list = []
        for index,i in enumerate(v):
            if(i == 1):
                temp_list.append(mylists[index])
        res_list.append(temp_list)
    return res_list

if __name__ == '__main__':
    m,n = map(lambda x:int(x),raw_input().split(" "))
    mylists = map(lambda x:int(x),raw_input().split(" ")) # 数字列表
    comb_list = combinations(mylists,m,n)
    for comb in comb_list:
        print(" ".join(map(lambda x:str(x),comb)))
