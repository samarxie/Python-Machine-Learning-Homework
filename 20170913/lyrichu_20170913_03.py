#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/13 11:44
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170913_03.py
'''
@Description:
Q3:
   顺时针打印矩阵。举例：
    1  2  3  4
    5  6  7  8
    9 10 11 12
   13 14 15 16

输出为：1、2、3、4、8、12、16、15、14、13、9、5、6、7、11、10
'''

# 打印一圈
def getCycle(start,n,num):
    '''
    :param start: 开始的数字
    :param n: 矩阵的边长
    :param num: 一圈的长度
    :return: 顺时针一圈下来数字列表
    '''
    res_list = [start+i for i in range(num)]  # 第一条边
    # 第二条边
    temp = res_list[-1]
    for i in range(1,num):
        res_list.append(temp + n*i)
    # 第三条边
    temp = res_list[-1]
    for i in range(1,num):
        res_list.append(temp-i)
    # 第四条边
    temp = res_list[-1]
    for i in range(1,num-1):
        res_list.append(temp-n*i)
    return res_list

# 顺时针打印
def clockWise(n):
    '''
    :param n: 矩阵边长
    :return: 顺时针打印列表
    '''
    length = 0 # 已经打印的边数
    res_list = []
    start = 1
    num = n
    while(length < n):
        mylist = getCycle(start,n,num)
        res_list.extend(mylist)
        length += 2
        num -= 2
        start = mylist[-1] + 1
    return res_list

if __name__ == '__main__':
    n = int(raw_input())   # 矩阵的边长
    res_list = clockWise(n)
    print(",".join(map(lambda x:str(x),res_list)))
