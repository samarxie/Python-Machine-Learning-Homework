# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q2：
度度熊最近对全排列特别感兴趣,对于1到n的一个排列,度度熊发现可以在中间根据大小关系插入合适的大于和小于符号(即 '>' 和 '<' )使其成为一个合法的不等式数列。但是现在度度熊手中只有k个小于符号即('<'')和n-k-1个大于符号(即'>'),
度度熊想知道对于1至n任意的排列中有多少个排列可以使用这些符号使其为合法的不等式数列。
输入描述:
输入包括一行,包含两个整数n和k(k < n ≤ 1000)
输出描述:
输出满足条件的排列数,答案对2017取模。
示例1
输入
5 2
输出
66
'''
def counts_by_dp(n,k):
	'''
	dp(动态规划求解)
	:param n: 正整数n
	:param k: '<' 符号个数
	:return 所有方法数
	'''
	# arr[i][j] 表示 n=i,k=j时的方法数目
	arr = [[0]*(k+1) for _ in range(n+1)]
	arr[1][0] = 1 # n=1,k=0的情况 
	for i in range(2,n+1):
		for j in range(k+1):
			if(j == 0):
				arr[i][j] = 1
			else:
				arr[i][j] = arr[i-1][j-1] + arr[i-1][j] + j*arr[i-1][j] + (i-j-1)*arr[i-1][j-1]
	return arr[n][k] % 2017
if __name__ == '__main__':
	n,k = map(int,input().split(" "))
	print(counts_by_dp(n,k))
	
	