# -*- coding:utf-8 -*-
'''
Q3：
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
思路参考:http://www.cnblogs.com/pmars/archive/2013/12/04/3458289.html
'''

# 全排列字典排序打印(非递归形式)
def string_dict_order_print(string):
	# 将 string 变为列表
	string = list(string)
	length = len(string)
	# 排序
	string.sort()
	# 字典排序最大字符串(从高到低排序)
	string_reverse = list(reversed(string))
	while(string != string_reverse):
		print("".join(string))
		index = length-1
		while(index>=1 and string[index-1] > string[index]):
			index -= 1
		max_index = length - 1
		while(max_index >= index and string[max_index] < string[index-1]):
			max_index -= 1
		# 交换
		string[index-1],string[max_index] = string[max_index],string[index-1]
		string = string[:index] + list(reversed(string[index:]))
	print("".join(string))
	
# 递归版本
def recursion_dict_order(string_list,from_index,end_index):
	if from_index == end_index:
		print("".join(string_list))
	else:
		for i in range(from_index,end_index+1):
			# 重新排序
			string_list = string_list[:from_index] + sorted(string_list[from_index:end_index+1])
			string_list[from_index],string_list[i] = string_list[i],string_list[from_index]
			recursion_dict_order(string_list,from_index+1,end_index)
			string_list[from_index],string_list[i] = string_list[i],string_list[from_index]

if __name__ == '__main__':
	string = input("Please input a string:(only have alphabets)")
	print("The dict order permutation of \"%s\" is:" % string)
	string_dict_order_print(string)
	print("The dict order permutation of \"%s\" using recursion method is:" % string)
	recursion_dict_order(list(string),0,len(string)-1)
	