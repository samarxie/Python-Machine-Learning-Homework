# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q2:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

def merge_ksorted_lists(klists):
	'''
	:param klists: k sorted lists in a list
	:return total sorted lists
	'''
	# k is the num of sorted lists
	k = len(klists)
	total_lists = klists[0]
	if(k > 1):
		for lists in klists[1:]:
			total_lists.extend(lists)
	total_lists.sort()
	return total_lists
	
if __name__ == '__main__':
	klists = []
	print("Please input a sorted number lists:")
	_input = input()
	while(_input):
		lists = [int(i) for i in _input.split(" ")]
		klists.append(lists)
		print("Please input a sorted number lists:")
		_input = input()
	print("Your input is:")
	for lists in klists:
		print(" ".join(map(str,lists)))
	total_sorted_lists = merge_ksorted_lists(klists)
	print("The merged sorted lists is:{}".format(" ".join(map(str,total_sorted_lists))))
	