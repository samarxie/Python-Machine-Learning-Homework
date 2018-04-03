# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q1:一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
def jump_step_by_recursion(n):
	'''
	通过递归来解(n 很大时，递归过深，求解速度极慢)
	:param n: 台阶个数
	:return: 总跳法数
	'''
	if(n == 1):
		return 1
	elif(n == 2):
		return 2
	else:
		return jump_step_by_recursion(n-1) + jump_step_by_recursion(n-2)

def jump_step_by_iteration(n):
	'''
	通过迭代来解(即使n很大，求解速度也很快)
	:param n: 台阶个数
	:return: 总跳法数
	'''
	# 设f(n) 为台阶数为n时的跳法数，利用递推公式 f(1)=1,f(2)=2,f(n) = f(n-1) + f(n-2)(n>2)来求解
	if(n == 1 or n == 2):
		return n
	else:
		a1,a2 = 1,2
		for _ in range(n-2):
			a1,a2 = a2,a1+a2
	return a2

if __name__ == '__main__':
	n = int(input())
	print(jump_step_by_recursion(n))
	print(jump_step_by_iteration(n))