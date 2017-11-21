# -*- coding:utf-8 -*-
'''
操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:

二叉树的镜像定义：源二叉树 
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
'''
class Node():
	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right
		
class BinaryTree():
	def __init__(self):
		self.root = Node()
		self.node_list = []
	
	# 增加节点
	def add_node(self,data):
		if(isinstance(data,(int,float))):
			if(self.root.data == None):
				self.root.data = data
				self.node_list.append(self.root)
			else:
				new_node = Node(data)
				current_node = self.node_list[0]
				if(current_node.left == None):
					current_node.left = new_node
					self.node_list.append(current_node.left)
				else:
					current_node.right = new_node
					self.node_list.append(current_node.right)
					self.node_list.pop(0)
		elif(isinstance(data,list)):
			for item in data:
				self.add_node(item)
	
	# 前序遍历
	def pre_print(self,root):
		if(root == None):
			return
		print(root.data,end=" ")
		self.pre_print(root.left)
		self.pre_print(root.right)
		
	# 中序遍历
	def mid_print(self,root):
		if(root == None):
			return
		self.mid_print(root.left)
		print(root.data,end=" ")
		self.mid_print(root.right)
		
	# 后序遍历
	def back_print(self,root):
		if(root == None):
			return
		self.back_print(root.left)
		self.back_print(root.right)
		print(root.data,end=" ")
	
	# 层次遍历
	def level_print(self,root):
		list_ = []
		if(root.data == None):
			print("This is an empty binary tree!")
		else:
			list_.append(root)
			while(list_):
				current_node = list_.pop(0)
				print(current_node.data,end=" ")
				if(current_node.left):
					list_.append(current_node.left)
				if(current_node.right):
					list_.append(current_node.right)

# 求二叉树的镜像树
def mirror_tree(root):
	if(root == None):
		return
	# 如果左右子树都为空
	if(root.left == None and root.right == None):
		return
	# 交换左右子树
	root.left,root.right = root.right,root.left
	if(root.left):
		mirror_tree(root.left)
	if(root.right):
		mirror_tree(root.right)

if __name__ == '__main__':
	binary_tree = BinaryTree()
	binary_tree.add_node([1,3,4,5,10])
	print("前序遍历:")
	binary_tree.pre_print(binary_tree.root)
	print("\n中序遍历:")
	binary_tree.mid_print(binary_tree.root)
	print("\n后序遍历:")
	binary_tree.back_print(binary_tree.root)
	print("\n层次遍历:")
	binary_tree.level_print(binary_tree.root)
	print("")
	# 求镜像二叉树
	mirror_tree(binary_tree.root)
	print("镜像二叉树前序遍历为:")
	binary_tree.pre_print(binary_tree.root)
	print("")
	
	
	
			
	
	