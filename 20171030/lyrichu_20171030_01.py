# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q1:
一个只包含'A'、'B'和'C'的字符串，如果存在某一段长度为3的连续子串中恰好'A'、'B'和'C'各有一个，那么这个字符串就是纯净的，否则这个字符串就是暗黑的。例如：
BAACAACCBAAA 连续子串"CBA"中包含了'A','B','C'各一个，所以是纯净的字符串
AABBCCAABB 不存在一个长度为3的连续子串包含'A','B','C',所以是暗黑的字符串
你的任务就是计算出长度为n的字符串(只包含'A'、'B'和'C')，有多少个是暗黑的字符串。
输入一个整数n，表示字符串长度(1 ≤ n ≤ 30)
输出一个整数表示有多少个暗黑字符串
'''

def count_black_str(n):
	'''
	思路参考:https://uploadfiles.nowcoder.com/images/20160913/964976_1473736361531_560EE1C917735D766A0A56AC2EFBB34A
	关键是找出递推公式
	:param n: 字符串长度
	:return: 暗黑字符串个数
	'''
	if(n == 1):
		return 3
	elif(n == 2):
		return 9 
	else:
		# counts[i] 表示长度为i+1的字符串暗黑字符串个数
		counts = [3,9]
		for i in range(2,n):
			black_str_num = 2*counts[i-1] + counts[i-2]
			counts.append(black_str_num)
		return counts[n-1]
		
if __name__ == '__main__':
	n = int(input())
	print(count_black_str(n))
	