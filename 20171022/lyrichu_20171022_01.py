# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q1：
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

# 定义二叉树
class BinaryTree(object):
	def __init__(self,data,left,right):
		'''
		定义一棵二叉树
		:param data:根节点数据
		:param left: 左子树
		:param right: 右子树
		'''
		self.data = data
		self.left = left
		self.right = right

def rebuild_binarytree(pre,mid):
	'''
	根据前序遍历和中序遍历的结果重建二叉树
	:param pre: 前序遍历
	:param mid: 中序遍历
	'''
	if(len(pre) == 0):
		return None
	# 根节点是前序遍历第一个
	root = pre[0]
	# 找到中序遍历序列中的根节点位置
	for i in range(len(mid)):
		if(root == mid[i]):
			break
	# 递归构造左右子树
	left = rebuild_binarytree(pre[1:i+1],mid[:i])
	right = rebuild_binarytree(pre[i+1:],mid[i+1:])
	return BinaryTree(root,left,right)
	

	
if __name__ == '__main__':
	# 前序遍历
	pre = [1,2,4,7,3,5,6,8]
	# 中序遍历
	mid = [4,7,2,1,5,3,8,6]
	root = rebuild_binarytree(pre,mid)
	
	
		
	