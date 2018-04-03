# -*- coding:utf-8 -*-
'''
Q1：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''
# 栈类
class Stack():
	def __init__(self):
		# 保存数据的栈
		self.stack = []
		# 保存最小元素的栈
		self.min_stack = []
	# 入栈操作
	def push(self,data):
		self.stack.append(data)
		# 如果 min_stack 为空，直接push
		if(len(self.min_stack) == 0):
			self.min_stack.append(data)
		else:
			top_data = self.min_stack.pop()
			push_data = top_data if top_data < data else data
			self.min_stack.append(push_data)
			
	# 弹出栈顶元素
	def top(self):
		return self.stack.pop()
	
	# 得到 栈最小元素 
	def stack_min(self):
		return self.min_stack.pop()
		
	
if __name__ == '__main__':
	my_stack = Stack()
	my_stack.push(1)
	my_stack.push(3)
	my_stack.push(0)
	my_stack.push(-9)
	# 得到栈最小元素
	s_min = my_stack.stack_min()
	print("栈最小元素为",s_min)
	
	