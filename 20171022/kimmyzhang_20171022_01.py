#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20171022_01.py
@Time: 2017/10/22 11:48
"""


import random


class Node(object):

    def __init__(self, label = -1, left_child = None, right_child = None):
        self.label = label
        self.left_child = left_child
        self.right_child = right_child

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_left(self):
        return self.left_child

    def set_left(self, left_child):
        self.left_child = left_child

    def get_right(self):
        return self.right_child

    def set_right(self, right_child):
        self.right_child = right_child


# store in order
class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    # 检验是否为空函数，十分有必要，写上
    def is_empty(self):
        # 针对None这样的类别判断，使用的是is。
        if self.root is None:
            return True
        return False

    def insert(self, label):

        # 新建节点
        node = Node(label)

        if self.is_empty():
            self.root = node
        else:
            dad_node= None
            curr_node = self.root

            # 有什么意思呢？为什么总是while true？是不是因为只有break掉，才会有意义呢？
            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node.get_label() < curr_node.get_label():
                        curr_node = curr_node.get_left()
                    else:
                        curr_node = curr_node.get_right()
                else:
                    if node.get_label() < dad_node.get_label():
                        dad_node.set_left(node)
                    else:
                        dad_node.set_right(node)
                    break

    def pre_show(self, curr_node):
        if curr_node is Node:
            # end = " " of the line is uncertain
            print(curr_node.get_label(), end = " ")
            self.pre_show(curr_node.get_left())
            self.pre_show(curr_node.get_right())

    def get_root(self):
        return self.root

    def front_recursion(self, root):
        if root is None:
            return
        print(root.label)
        self.front_recursion(root.left_child)
        self.front_recursion(root.right_child)


if __name__ == '__main__':
    elements = [random.randint(1,10) for _ in range(10)]
    # print(elements)
    bst = BinarySearchTree()
    for element in elements:
        bst.insert(element)

    bst.front_recursion(bst.root)