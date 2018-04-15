#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-04-15 08:40:54
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
已知一个排序数组,给定一个时间窗口值,求数组每个元素
在前后给定时间窗口内包含的元素个数(包括自身)
例如,给定时间窗口N = 2,对于数组a = [1,3,4,7,8,10]
输出为[2,3,2,2,3,2]
'''
def solution(arr,N):
	total = len(arr) # 数组总长度
	p = 0 # 指向当前位置时间窗口指针
	p1 = 0 # 指向左时间窗口边界指针
	p2 = 0 # 指向右时间窗口边界指针
	for p2 in range(1,total):
		if arr[p2]-arr[p] > N:
			break
	p2 -= 1
	res = [p-p1+1+p2-p]
	p += 1
	while p < total:
		while p1 <=p and arr[p]-arr[p1] > N:
			p1 += 1
		flag = False
		while p2 < total and arr[p2]-arr[p] <= N:
			flag = True
			p2 += 1
		if flag:
			p2 -= 1
		res.append(p-p1+1+p2-p)
		p += 1
	return res 

if __name__ == '__main__':
	a = [1,3,4,7,8,9,10,22]
	N = 2
	res = solution(a,N)
	print(res)

