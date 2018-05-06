#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-04-17 15:26:50
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
Q1:利用栈实现二叉树的非递归形式的前,中,后序遍历
'''
class Node:
	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

class BinaryTree:
	def __init__(self):
		self.root = Node()
		self.stack = []

	def order_insert(self,data):
		'''
		二叉树顺序插入
		'''
		if self.root.data is None:
			self.root.data = data
			self.stack.append(self.root)
		else:
			new_node = Node(data)
			cur_node = self.stack[0]
			if cur_node.left is None:
				cur_node.left = new_node
				self.stack.append(cur_node.left)
			else:
				cur_node.right = new_node
				self.stack.append(cur_node.right)
				self.stack.pop(0) #去除根节点

	def recursion_pre_print(self,root):
		if root is None:
			return
		print(root.data,end = " ")
		self.recursion_pre_print(root.left)
		self.recursion_pre_print(root.right)

	def recursion_mid_print(self,root):
		if root is None:
			return
		self.recursion_mid_print(root.left)
		print(root.data,end = " ")
		self.recursion_mid_print(root.right)

	def recursion_back_print(self,root):
		if root is None:
			return
		self.recursion_back_print(root.left)
		self.recursion_back_print(root.right)
		print(root.data,end = " ")

	def recursion_level_print(self):
		if self.root.data is None:
			print("This is an empty tree!")
		print(self.root.data,end = " ")
		level_stack = [self.root]
		while level_stack:
			cur_node = level_stack.pop(0)
			if cur_node.left:
				print(cur_node.left.data,end = " ")
				level_stack.append(cur_node.left)
			if cur_node.right:
				print(cur_node.right.data,end = " ")
				level_stack.append(cur_node.right)

	def stack_pre_print(self):
		'''
		非递归前序遍历
		'''
		stack = []
		cur_node = self.root
		if cur_node.data is None:
			print("This is an empty tree!")
		while stack or cur_node:
			while cur_node:
				print(cur_node.data,end = " ")
				# 左子树入栈
				stack.append(cur_node)
				cur_node = cur_node.left
			# 开始查看右子树
			cur_node = stack.pop()
			cur_node = cur_node.right

	def stack_mid_print(self):
		'''
		非递归中序遍历
		'''
		stack = []
		cur_node = self.root
		if cur_node.data is None:
			print("This is an empty tree!")
		while cur_node or stack:
			# 左子树一直入栈
			while cur_node:
				stack.append(cur_node)
				cur_node = cur_node.left
			cur_node = stack.pop()
			print(cur_node.data,end = " ")
			# 查看右子树
			cur_node = cur_node.right

	def stack_back_print(self):
		'''
		非递归后序遍历
		'''
		stack = [] 
		stack_print = [] # 最终的遍历打印栈
		cur_node = self.root
		stack.append(self.root)
		while stack:
			cur_node = stack.pop()
			if cur_node.left:
				stack.append(cur_node.left)
			if cur_node.right:
				stack.append(cur_node.right)
			stack_print.append(cur_node)
		while stack_print:
			print(stack_print.pop().data,end = " ")









if __name__ == '__main__':
	tree = BinaryTree()
	data = range(1,11)
	for d in data:
		tree.order_insert(d)
	print("递归前序遍历:",end = " ")
	tree.recursion_pre_print(tree.root)
	print("\n")
	print("非递归先序遍历:",end = " ")
	tree.stack_pre_print()
	print("\n")
	print("递归中序遍历:",end = " ")
	tree.recursion_mid_print(tree.root)
	print("\n")
	print("非递归中序遍历:",end = " ")
	tree.stack_mid_print()
	print("\n")
	print("递归后序遍历:",end = " ")
	tree.recursion_back_print(tree.root)
	print("\n")
	print("非递归后序遍历:",end = " ")
	tree.stack_back_print()
	print("\n")
	print("层次遍历:",end = " ")
	tree.recursion_level_print()
	print("\n")


