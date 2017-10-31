# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q1:
最大连续和问题。
给出一个长度为n的序列A1, A2,…, An，求最大连续和。
换句话说，要求找到1≤i≤j≤n，使得A1 + …, Aj尽量大.
'''
def find_max_sum(nums):
	'''
	:param nums:数字列表
	:return: 最大连续和
	'''
	# 初始化最大连续和为负无穷
	max_sum = -float('inf')
	# 初始化和为0
	_sum = 0
	for i in nums:
		# 如果之前的和大于等于0，则继续相加
		if(_sum >=0):
			_sum += i 
		# 否则从当前数开始加
		else:
			_sum = i
		# 更新最大连续和
		if(_sum > max_sum):
			max_sum = _sum
	return max_sum
	
if __name__ == '__main__':
	nums = list(map(int,input().split(" ")))
	print("最大连续和为:",find_max_sum(nums))
	
			
