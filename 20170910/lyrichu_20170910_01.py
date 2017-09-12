#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/11 7:04
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170910_01.py
'''
@Description:
使用python类实现一个双向链表结构，并且实现增删查改等基本操作。
参考自:http://www.cnblogs.com/yupeng/p/3413800.html
'''

# 定义一个节点
class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p
        self.prev = p
# 定义双向链表
class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key <0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print 'linklist is empty.'
            return

        elif key <0  or key > self.getlength():
            print 'the given key is error'
            return

        else:
            self.delete(key)
            return self.insert(key,value)
    # 初始化链表
    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            node.prev  = p
            p = p.next
    # 获得数组长度
    def getlength(self):
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length
    # 判断数组是否为空
    def is_empty(self):
        if self.getlength() ==0:
            return True
        else:
            return False
    # 清空数组
    def clear(self):
        self.head = 0

    # 向链表中增加一个元素
    def append(self,item):
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q
            q.prev = p

    # 获得索引index处的节点值
    def getitem(self,index):
        if self.is_empty():
            print 'Linklist is empty.'
            return
        j = 0
        p = self.head
        while p.next!=0 and j <index:
            p = p.next
            j+=1
        if j ==index:
            return p.data
        else:
            print 'target is not exist!'
    # 在index处插入值item
    def insert(self,index,item):
        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            q = Node(item,p)
            post.next = q
            q.prev = post
            q.next = p
            p.prev = q

    # 删除index处的节点
    def delete(self,index):
        if self.is_empty() or index<0 or index >self.getlength():
            print 'Linklist is empty.'
            return
        if index ==0:
            if(self.getlength() > 1):
                item = self.getitem(1)
                q = Node(item,self.head)
                self.head = q
            else:
                self.clear()
                return
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            post.next = p.next
            p.next.prev = post
    # 返回 value值的索引
    def index(self,value):
        if self.is_empty():
            print 'Linklist is empty.'
            return
        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1
        if p.data == value:
            return i
        else:
            return -1

if __name__ == '__main__':
    # 一些 实例
    l = LinkList()
    l.initlist([1,2,3,4,5])
    print l.getitem(4)
    l.append(6)
    print l.getitem(5)
    l.insert(4,40)
    print l.getitem(3)
    print l.getitem(4)
    print l.getitem(5)
    l.delete(5)
    print l.getitem(5)
    l.index(5)
