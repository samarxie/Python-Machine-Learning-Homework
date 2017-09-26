#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170915_01.py
@time: 2017/9/25 21:09
@description:使用python实现二叉排序树(二叉查找树)
"""
class BinarySearchTree():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def find(self,x):
        '''
        查找
        :param x: 查找的数据
        :return: 如果数据存在，返回查找到的节点；否则返回None
        '''
        if(x == self.key):
            return self
        elif(x<self.key and self.left):
            return self.left.find(x)
        elif(x > self.key and self.right):
            return self.right.find(x)
        else:
            return None

    def findMin(self):
        '''
        查找二叉树中最小元素的位置
        :return:二叉树中最小元素的位置
        '''
        # 如果左子树存在，则递归查找左子树
        if(self.left):
            return self.left.findMin()
        # 如果左子树不存在，则返回根节点
        else:
            return self

    def findMax(self):
        '''
        查找二叉树中最大元素的位置
        :return: 二叉树中最大元素的位置
        '''
        tree = self
        if(tree):
            # 如果右子树存在，则递归查找右子树
            while(tree.right):
                tree = tree.right
        return tree

    def insert(self,x):
        '''
        插入操作：如果查找到x，则什么也不做；如果没有查找到，则将x插入到遍历路径的最后一点
        :param x: 被插入的数据
        :return: None
        '''
        if(x < self.key):
            # 如果左子树存在，则遍历插入数据到左子树
            if(self.left):
                self.left.insert(x)
            else:
                # 如果左子树不存在，则将该数据插入到根节点的左节点
                self.left = BinarySearchTree(x)
        elif(x > self.key):
            if(self.right):
                self.right.insert(x)
            else:
                self.right = BinarySearchTree(x)

    def delete(self,x):
        '''
        删除某个节点，分为三种情况：
        1.如果删除的节点为叶子结点，则直接删除
        2.如果该节点只有一个儿子节点，则将此节点的父节点的指针指向此节点的儿子，然后将该节点删除
        3.如果该节点左节点和右节点均存在，则将该节点的数据替换为右子树的最小数据，然后将该最小数据的节点删除
        :param x:待删除的数据
        :return:删除完数据之后的树
        '''
        if(self.find(x)):
            # 如果数据小于根节点，则遍历删除左子树
            if(x < self.key):
                self.left = self.left.delete(x)
                return self
            elif(x > self.key):
                self.right = self.right.delete(x)
                return self
            elif(self.left and self.right):
                key = self.right.findMin().key
                self.key = key
                self.right = self.right.delete(key)
                return self
            else:
                if(self.left):
                    return self.left
                else:
                    return self.right
        else:
            return self




