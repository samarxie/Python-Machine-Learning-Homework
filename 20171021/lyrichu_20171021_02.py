# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
def jump_step(n):
	'''
	迭代求解跳台阶总方法数
	:param n: 台阶数目
	:return: 跳台阶总方法数
	'''
	if(n == 1 or n == 2):
		return n
	else:
		# methods[] 第i个元素存放台阶数为i+1时的方法数
		methods = []
		for i in range(1,n+1):
			if(i == 1 or i == 2):
				methods.append(i)
			else:
				methods.append(sum(methods)+1)
		return methods[-1]

if __name__ == '__main__':
	n = int(input())
	print(jump_step(n))