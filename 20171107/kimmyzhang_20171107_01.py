#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171107_01.py
@Time: 2017/11/16 16:33
Q1:
    输入一个链表，输出该链表中倒数第k个结点。
"""


# 从自己写的包中导入了类
from Demo_data_algo.Data.LinkedList.linkedlist import LinkList


def back_k_num(nums, k):
    '''
    链表倒数第k个节点
    :param nums: 数组
    :param k: k
    :return: result
    '''

    # 初始化类
    test_list = LinkList()
    # 将数组传入
    test_list.initlist(nums)
    node_1st = test_list.head
    node_2nd = test_list.head

    # 控制两个节点的间距
    interval = 1

    while node_2nd.next != 0 and interval < k:
        node_2nd = node_2nd.next
        interval += 1

    while node_2nd.next != 0:
        node_1st = node_1st.next
        node_2nd = node_2nd.next

    return node_1st.val


if __name__ == '__main__':
    nums = [1, 5, 3, 4, 2, 0, 10]
    k = 7
    result = back_k_num(nums, k)
    print(result)