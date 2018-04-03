# -*- coding:utf-8 -*-
'''
update in 2017-10-30
@author:lyrichu
@email:919987476@qq.com
@description:
Q2:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 
'''

def merge_k_lists(klists):
	'''
	采用两两合并的方式将k个有序列表合并
	:param klists: k个待归并的有序列表
	:return: 归并之后的有序列表
	'''
	k = len(klists)
	while(k > 1):
		for i in range(k//2):
			klists[i] = merge_two_lists(klists[i],klists[i+(k+1)//2])
		k = (k+1)//2 
	# 最终只有一个排序好的列表
	return klists[0]
	
def merge_two_lists(list1,list2):
	'''
	合并两个有序列表
	:param list1: 有序列表1
	:param list2: 有序列表2
	:return: 归并之后的有序列表
	'''
	# 归并之后的有序列表
	new_list = []
	while(len(list1) > 0 and len(list2) > 0):
		# 分别取list1和list2的第一个数进行比较，将数字较小的放入归并列表,并且删除该数字
		# 直到有一个列表为空
		if(list1[0] <= list2[0]):
			new_list.append(list1[0])
			list1.pop(0)
		else:
			new_list.append(list2[0])
			list2.pop(0)
	# 将剩下的长度不为0的列表添加到new_list的尾部
	if(len(list1) > 0):
		new_list.extend(list1)
	if(len(list2) > 0):
		new_list.extend(list2)
	return new_list
	
if __name__ == '__main__':
	klists = []
	_input = input()
	while(_input):
		lists = list(map(int,_input.split(" ")))
		klists.append(lists)
		_input = input()
	print(merge_k_lists(klists))
	