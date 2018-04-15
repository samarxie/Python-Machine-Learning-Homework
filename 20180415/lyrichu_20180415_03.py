#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-04-15 09:41:05
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
给定一个数组,设计一个时间复杂度为O(nlgn)的算法求数组的第k大数字
'''
import random 

def solution(k,arr,begin,end):
	if begin >= end:
		return arr[begin]
	i = begin 
	j = end
	key = begin 
	while i < j:
		while i < j and arr[j] >= arr[key]:
			j -= 1
		# 交换key和j位置的元素
		if i < j:
			arr[key],arr[j] = arr[j],arr[key]
			key = j
		while i < j and arr[i] <= arr[key]:
			i += 1
		if i < j:
			arr[key],arr[i] = arr[i],arr[key]
			key = i
	if key == len(arr)-k:
		return arr[key]
	if key < len(arr)-k:
		return solution(k,arr,key+1,end)
	if key > len(arr)-k:
		return solution(k,arr,begin,key-1)

if __name__ == '__main__':
	k = 4
	N = 10000000
	arr = list(range(1,N+1))
	random.shuffle(arr) # 随机打乱数组
	res = solution(k,arr,0,N-1)
	print("arr中第%d大的数字是:%d" %(k,res))