#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-05-05 12:06:56
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
Q2:(深度优先搜索,dfs)
描述
给出一个正整数 n, 请输出 n 的所有全排列
输入
一个整数 n(1 ≤ n ≤ 10)
输出
一共 n! 行,每行 n 个用空格隔开的数,表示 n 的一个全排列。并且按全排列的字典序输出。
样例输入
3
样例输出
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
def dfs(history,i):
	'''
	@param history:记录每个位置的数字
	@param i:第i个位置填数
	'''
	if i == len(history):
		for v in history:
			print(v,end = " ")
		print("")
		return
	# 第i个位置填数
	for k in range(1,len(history)+1):
		ok = True # 判断所填数字是否非法
		for j in range(i):
			if history[j] == k: # i,j位置数字相同
				ok = False
		if ok:
			history[i] = k
			dfs(history,i+1)

if __name__ == '__main__':
	N = int(input())
	history = [0]*N 
	dfs(history,0)

