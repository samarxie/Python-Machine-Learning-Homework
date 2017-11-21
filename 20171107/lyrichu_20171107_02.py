# -*- coding:utf-8 -*-
'''
Q2:输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

def number_of_1(n):
	# count 为 二进制中1的个数
	count = 0
	# 从n的二进制最右边开始判断是不是1
	flag = 1
	index = 0
	while(index < 32):
		if(n&flag):
			count += 1
		# 左移一位
		flag <<= 1
		index += 1
	return count
	
if __name__ == '__main__':
	n = int(input("Please input an integer:"))
	print("The count of 1 in %d of binary is %d" %(n,number_of_1(n)))
	
	
		