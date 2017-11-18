#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171108_01.py
@Time: 2017/11/18 21:15
Q1:
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
from Demo_data_algo.Data.LinkedList.linkedlist import LinkList


def solution_linkedlist(nums):
    '''
    使用链表
    也可以直接在一个链表上进行操作
    :param nums:
    :return: 将奇数链表和偶数链表进行连接
    '''
    chain = LinkList()
    chain.initlist(nums)

    # 分别存储奇偶项
    store_odd = LinkList()
    store_even = LinkList()

    node = chain.head
    while node != 0:
        if node.val % 2 == 0:
            store_even.append(node.val)
        else:
            store_odd.append(node.val)
        node = node.next

    return 0


def solution_list(nums):
    li = nums
    li_even = []
    li_odd = []
    for num in nums:
        if num % 2 == 0:
            li_even.append(num)
        else:
            li_odd.append(num)

    return li_odd + li_even


if __name__ == '__main__':
    nums = [2,4,1,5,8,2]
    # result1 = solution_linkedlist(nums)
    result2 = solution_list(nums)
    print(result2)