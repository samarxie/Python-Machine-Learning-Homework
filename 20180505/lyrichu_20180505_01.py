#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-05-05 11:23:28
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
Q1:
描述
给定 N (N ≤ 8) 个点的地图,以及地图上各点的相邻关系,请输出用 4 种颜色将地图涂色的所
有方案数(要求相邻两点不能涂成相同的颜色)
。
数据中 0 代表不相邻,1 代表相邻。
输入
第一行一个整数 N ,代表地图上有 N 个点。
接下来 N 行,每行 N 个整数,每个整数是 0 或者 1。第 i 行第 j 列的值代表了第 i 个点和第 j 个
点之间是相邻的还是不相邻,相邻就是 1,不相邻就是 0。我们保证 a[i][j] = a[j][i]。
输出
染色的方案数
样例输入
0 0 0 1 0 0 1 0
0 0 0 0 0 1 0 1
0 0 0 0 0 0 1 0
1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0
1 0 1 0 0 0 0 0
0 1 0 0 0 0 0 0
样例输出
15552
'''
def dfs(matrix,history,i):
	'''
	@param matrix:表示地点位置关系的矩阵
	@param history:记录染色方案的list
	@param i:第i个地点
	'''
	global count
	if i == len(matrix[0]):
		count += 1
		return
	# 对第i个地点进行染色
	# 四种颜色分别用1,2,3,4表示
	for c in range(1,5):
		ok = True # 判断染色是否可行
		for j in range(i):
			if history[j] == c and matrix[i][j] == 1: # 相邻且同色
				ok = False
		if ok:
			history[i] = c  # 第i个地点染c这种颜色
			dfs(matrix,history,i+1) # 继续给i+1染色

if __name__ == '__main__':
	count = 0
	N = int(input())
	matrix = [0]*N 
	history = [0]*N 
	for i in range(N):
		matrix[i] = list(map(int,input().split()))
	dfs(matrix,history,0)
	print(count)



 