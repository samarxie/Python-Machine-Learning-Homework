#-*- coding:utf-8 -*-
'''
Q3：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

class Node():
	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right
		
class Binarytree():
	def __init__(self):
		self.root = Node()
		self.node_list = []
		# 存放满足条件的路径列表
		self.path_list = []
		# 一个满足条件的路径
		self.path = []
		
	def add_node(self,data):
		if isinstance(data,(int,float)):
			if self.root.data == None:
				self.root.data = data
				self.node_list.append(self.root)
			else:
				current_node = self.node_list[0]
				new_node = Node(data)
				if current_node.left == None:
					current_node.left = new_node
					self.node_list.append(current_node.left)
				else:
					current_node.right = new_node
					self.node_list.append(current_node.right)
					self.node_list.pop(0)
		elif isinstance(data,list):
			for item in data:
				self.add_node(item)
				
	def pre_print(self,root):
		if root == None:
			return
		print(root.data,end=" ")
		self.pre_print(root.left)
		self.pre_print(root.right)
		
	def mid_print(self,root):
		if root == None:
			return
		self.mid_print(root.left)
		print(root.data,end=" ")
		self.mid_print(root.right)
		
	def back_print(self,root):
		if root == None:
			return
		self.back_print(root.left)
		self.back_print(root.right)
		print(root.data,end=" ")
		
	def find_path(self,root,target):
		'''
		:param root: 输入二叉树根节点
		:param target: 剩余目标数字
		:return: 所有满足条件的路径
		'''
		if root == None:
			return
		self.path.append(root.data)
		# 如果目前根节点的值和剩余目标数字相等，且当前节点为叶子节点
		# 则找到一个满足条件的路径
		target -= root.data
		print(self.path)
		if target == 0 and root.left == None and root.right == None:
			self.path_list.append([i for i in self.path]) # 注意这里需要append 一个新的path，否则后面的pop 会影响结果
		self.find_path(root.left,target)
		self.find_path(root.right,target)
		self.path.pop()
		
		
		
		
	
	
	
if __name__ == '__main__':
	binary_tree = Binarytree()
	binary_tree.add_node([1,2,3,1])
	print("前序遍历:\n")
	binary_tree.pre_print(binary_tree.root)
	print("")
	print("中序遍历:\n")
	binary_tree.mid_print(binary_tree.root)
	print("")
	print("后序遍历:\n")
	binary_tree.back_print(binary_tree.root)
	print("")
	binary_tree.find_path(binary_tree.root,target=4)
	print(binary_tree.path_list)
	
	
	