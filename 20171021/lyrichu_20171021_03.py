# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

def fill_rectangles(n):
	'''
	n个2*1的小矩形无重叠地覆盖一个2*n的大矩形,总方法数
	设 f(n) 为 总方法数，f(1) = 1,f(2) = 2, f(n) = f(n-1) + f(n-2)(n>=3)
	:param n: 整数n
	:return: 总方法数
	'''
	if(n == 0 or n == 1 or n == 2):
		return n 
	else:
		f1,f2 = 1,2
		for _ in range(n-2):
			f1,f2 = f2,f1+f2
		return f2

if __name__ == '__main__':
	n = int(input())
	print(fill_rectangles(n))
	