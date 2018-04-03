# -*- coding:utf-8 -*-
'''
Q2：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
# 二叉树节点类
class Node():
	def __init__(self,data = None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

# 二叉树类		
class Binarytree():
	def __init__(self):
		self.root = Node()
		# 存放节点的列表
		self.node_list = []
	
	#为二叉树增加节点
	def add_value(self,data):
		# 如果根节点为空
		if(not self.root.data):
			# 如果 data 是数字
			if(isinstance(data,(int,float))):
				self.root.data = data
				# 添加根节点
				self.node_list.append(self.root)
			# 如果是列表
			elif(isinstance(data,list)):
				if(data):
					for item in data:
						self.add_value(item)
		else:
			if(isinstance(data,(int,float))):
				# 新节点
				new_node = Node(data)
				current_node = self.node_list[0]
				# 如果左子树为空
				if(not current_node.left):
					current_node.left = new_node
					self.node_list.append(current_node.left)
				# 右子树为空
				else:
					current_node.right = new_node
					self.node_list.append(current_node.right)
					# 左右子树都已经填充，则丢弃父节点
					self.node_list.pop(0)
			elif(isinstance(data,list)):
				if(data):
					for item in data:
						self.add_value(item)
	
	# 前序遍历
	def pre_print(self,root):
		if(not root):
			return
		print(root.data,end=" ")
		self.pre_print(root.left)
		self.pre_print(root.right)
	# 中序遍历
	def mid_print(self,root):
		if(not root):
			return
		self.mid_print(root.left)
		print(root.data,end=" ")
		self.mid_print(root.right)
	# 后序遍历
	def back_print(self,root):
		if(not root):
			return
		self.back_print(root.left)
		self.back_print(root.right)
		print(root.data,end=" ")

# 判断 tree1 是否是 tree2 的子树		
def is_subtree(root1,root2):
	flag = False
	# tree1 是空树
	if(root1 and root2):
		# 如果 tree1 和 tree2 根节点值相同
		if(root1.data == root2.data):
			# 判断 tree1 是否 含有 tree2
			flag = tree1_has_tree2(root1,root2)
		if(not flag):
			flag = is_subtree(root1.left,root2)
		if(not flag):
			flag = is_subtree(root1.right,root2)
		return flag

# 判断 tree1 是否 含有 tree2
def tree1_has_tree2(root1,root2):
	if(root1 == None and root2 != None):
		return False
	if(root2 == None):
		return True
	if(root1.data != root2.data):
		return False
	return tree1_has_tree2(root1.left,root2.left) and tree1_has_tree2(root1.right,root2.right)
	
if __name__ == '__main__':
	binary_tree = Binarytree()
	binary_tree.add_value([1,2,3])
	binary_tree.add_value([4,10])
	print("前序遍历:")
	binary_tree.pre_print(binary_tree.root)
	print("\n中序遍历:")
	binary_tree.mid_print(binary_tree.root)
	print("\n后序遍历:")
	binary_tree.back_print(binary_tree.root)
	print("")
	binary_tree1 = Binarytree()
	binary_tree1.add_value([2,4,10])
	flag = is_subtree(binary_tree.root,binary_tree1.root)
	print("binary_tree1 %s binary_tree 的子树。" %("是" if flag else "不是"))
	

	
		
				
		