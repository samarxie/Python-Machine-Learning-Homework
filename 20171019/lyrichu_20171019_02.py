# -*- coding:utf-8 -*-
'''
我们把一个N位的数字等于其各位的N次方之和的数字称为阿姆斯特朗数，求100000以内的所有阿姆斯特朗数。
'''

def is_armstrong_number(n):
	'''
	判断一个数是否是阿姆斯特朗数
	:param n:数字n
	:return: True or False
	'''
	# 数字n的位数
	digits = len(str(n))
	# 各位数字列表
	numbers = map(int,list(str(n)))
	sum_ = sum(map(lambda x:x**digits,numbers))
	return sum_ == n
	
def find_armstrong_numbers(n):
	'''
	寻找小于n的所有armstrong数
	'''
	for i in range(n+1):
		if(is_armstrong_number(i)):
			print(i)
	
	
if __name__ == '__main__':
	find_armstrong_numbers(100000)
	
	
	