# -*- coding:utf-8 -*-
'''
Q2：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
class TreeNode():
	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right
		
class BinarySearchTree():
	def __init__(self):
		self.root = TreeNode()
		
	# 二叉搜索树插入
	def insert(self,root,data):
		if isinstance(data,(float,int)):
			if self.root.data == None:
				self.root.data = data
			else:
				if root == None:
					return
				if data < root.data:
					if root.left == None:
						root.left = TreeNode(data)
					else:
						self.insert(root.left,data)
				elif data > root.data:
					if root.right == None:
						root.right = TreeNode(data)
					else:
						self.insert(root.right,data)
		elif isinstance(data,list):
			for item in data:
				self.insert(root,item)
	
	# 中序遍历
	def mid_print(self,root):
		if root == None:
			return
		self.mid_print(root.left)
		print(root.data,end=" ")
		self.mid_print(root.right)
	
	# 将二叉搜索树转双向链表
	def convert_binary_to_link(self,root):
		if root == None:
			return
		# 左右子树都为空
		if root.left == None and root.right == None:
			return root
		# 先递归处理左子树
		left_node = self.convert_binary_to_link(root.left)
		temp_node = left_node
		# 遍历到left_node 的末尾节点
		while(temp_node != None and temp_node.right != None):
			temp_node = temp_node.right
		# 连接左子树与根节点
		if temp_node:
			temp_node.right = root
			root.left = temp_node
		# 处理右子树
		right_node = self.convert_binary_to_link(root.right)
		# 连接右子树与根节点
		if right_node:
			root.right = right_node
			right_node.left = root
		return left_node if left_node else root
		
	# 遍历转化之后的双向链表
	def link_print(self,root):
		while root:
			print(root.data,end=" ")
			root = root.right
		print("")
	
if __name__ == '__main__':
	binary_tree = BinarySearchTree()
	binary_tree.insert(binary_tree.root,[2,4,1,0,12,10])
	binary_tree.mid_print(binary_tree.root)
	print("")
	link_root = binary_tree.convert_binary_to_link(binary_tree.root)
	binary_tree.link_print(link_root)
	