# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q2：
从上往下打印出二叉树的每个节点，同层节点从左至右打印。(层次遍历)
'''
class Node(object):
  """节点类"""
  def __init__(self, elem=None, lchild=None, rchild=None):
    self.elem = elem
    self.lchild = lchild
    self.rchild = rchild

class Tree(object):
  """树类"""
  def __init__(self):
    self.root = Node()
    self.myQueue = []

  def add(self, elem):
    """为树添加节点"""
    node = Node(elem)
    if self.root.elem == None: # 如果树是空的，则对根节点赋值
      self.root = node
      self.myQueue.append(self.root)
    else:
      treeNode = self.myQueue[0] # 此结点的子树还没有齐。
      if treeNode.lchild == None:
        treeNode.lchild = node
        self.myQueue.append(treeNode.lchild)
      else:
        treeNode.rchild = node
        self.myQueue.append(treeNode.rchild)
        self.myQueue.pop(0) # 如果该结点存在右子树，将此结点丢弃。

  def level_queue(self, root):
    """利用队列实现树的层次遍历"""
    if root == None:
      return
    myQueue = []
    node = root
    myQueue.append(node)
    while myQueue:
      node = myQueue.pop(0)
      print(node.elem,)
      if node.lchild != None:
        myQueue.append(node.lchild)
      if node.rchild != None:
        myQueue.append(node.rchild)

if __name__ == '__main__':
  """主函数"""
  elems = range(10)      #生成十个数据作为树节点
  tree = Tree()     # 新建一个树对象
  for elem in elems:
    tree.add(elem)      #逐个添加树的节点
  print('队列实现层次遍历:')
  tree.level_queue(tree.root)
