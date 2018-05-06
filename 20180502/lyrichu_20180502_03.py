#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-05-05 16:22:39
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
Q3:给定一个链表a1->a2->...->an,返回a1->an->a2->a(n-1)->...
tips:将链表从中间一分为二,然后转换为链表插入问题
'''
class Node:
	def __init__(self,data = None,next_ = None):
		self.data = data
		self.next = next_

class LinkedList:
	def __init__(self):
		self.head = Node()

	def is_empty(self):
		return self.head.next is None

	def insert(self,data):
		new_node = Node(data)
		cur_node = self.head
		while cur_node.next:
			cur_node = cur_node.next
		cur_node.next = new_node

	def print(self):
		if self.is_empty():
			print("This is an empty linkedlist!")
		else:
			cur_node = self.head.next
			print(cur_node.data,end = " ")
			while cur_node.next:
				cur_node = cur_node.next
				print(cur_node.data,end = " ")
			print("")

	def length(self):
		if self.is_empty():
			return 0
		else:
			n = 0
			cur_node = self.head
			while cur_node.next:
				n += 1
				cur_node = cur_node.next
		return n 

def solution(linkedlist):
	n = linkedlist.length() # 链表长度
	cur_node = linkedlist.head
	index = 0
	while index < (n+1)//2:
		cur_node = cur_node.next
		index += 1
	cur_node1 = linkedlist.head.next
	cur_node2 = cur_node.next
	cur_node.next = None
	#linkedlist.print()
	tmp = [] # 辅助栈
	# 将第二个链表逆序
	while cur_node2:
		tmp.append(cur_node2)
		cur_node2 = cur_node2.next
	#print(len(tmp))
	while cur_node1.next and tmp:
		cur_node2 = tmp.pop() # 弹出栈
		cur_node2.next = None
		pre_node = cur_node1.next
		cur_node1.next = cur_node2
		cur_node2.next = pre_node
		cur_node1 = pre_node
	if tmp:
		cur_node1.next = tmp.pop()
		cur_node1.next.next = None







if __name__ == '__main__':
	li = LinkedList()
	for i in range(11):
		li.insert(i)
	# li.print()
	# print(li.length())
	solution(li)
	li.print()






