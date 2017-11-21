# -*- coding:utf-8 -*-
'''
Q1:
输入一个链表，输出该链表中倒数第k个结点。
'''
# 定义一个节点
class Node():
	def __init__(self,data=None):
		self.data = data
		self.next = None

# 定义一个链表		
class LinkList():
	def __init__(self,data):
		self.link_list = Node()
		self.append(data)
	
	# 为链表添加元素
	def append(self,data):
		# 如果 data 是整数
		if isinstance(data,(int,float)):
			# 新节点
			new_node = Node(data)
			node = self.link_list.next
			if(not node):
				self.link_list.next = new_node
				return
			else:
				while(node):
					pre = node
					node = node.next 
				pre.next = new_node
				return 
		# 如果 data 是列表
		elif isinstance(data,list):
			node = self.link_list.next
			while(data):
				item = data.pop(0)
				self.append(item)
			return
	
	# 打印链表数据
	def print_link_list(self):
		if(not self.link_list.next):
			print("This is an empty link list!")
		else:
			node = self.link_list.next 
			while(node):
				print(node.data,end = " ")
				node = node.next 
			print("")
	def print_endk_node(self,k):
		if(k<= 0):
			print("k must be a positive number!")
			return 
		else:
			# 如果是空链表
			if(not self.link_list.next):
				print("This is an empty link list!")
				return
			else:
				node1 = self.link_list.next
				node2 = node1
				# node1 先 遍历 k-1个节点
				index = 0
				while(node1.next and index < k-1):
					node1 = node1.next
					index += 1
				if(index != k-1):
					print("The link list is too short!")
					return 
				while(node1.next):
					node1 = node1.next
					node2 = node2.next
				print("The end kth node data is:",node2.data)
				return node2.data 
				
if __name__ == '__main__':
	link_list = LinkList(list(range(10)))
	link_list.print_link_list()
	link_list.append(1.3)
	link_list.print_link_list()
	link_list.print_endk_node(4)
	
	
				