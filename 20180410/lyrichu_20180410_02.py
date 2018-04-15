#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-04-10 20:34:42
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
Q2:
有股神吗？
有，小赛就是！
经过严密的计算，小赛买了一支股票，他知道从他买股票的那天开始，股票会有以下变化：第一天不变，以后涨一天，跌一天，涨两天，跌一天，涨三天，跌一天...依此类推。
便计算，假设每次涨和跌皆为1，股票初始单价也为1，请计算买股票的第n天每股股票值多少钱？
输入
输入包括多组数据；
每行输入一个n，1<=n<=10^9 。
输出
请输出他每股股票多少钱，对于每组数据，输出一行。
样例输入
1
2
3
4
5
样例输出
1
2
1
2
3
'''
def solution(n):
	# 动态规划求解
	# n是第n天
	s = [1]
	rise_index = 1 # 涨的第多少天
	days = 1 # 第多少天
	while days < n:
		index = rise_index
		while index > 0:
			s.append(s[-1]+1)
			days += 1
			index -= 1
		s.append(s[-1]-1)
		days += 1
		rise_index += 1
	return s[n-1]


if __name__ == '__main__':
	n = int(input())
	res = [n]
	while n:
		s = input()
		if s:
			n = int(s)
			res.append(n)
		else:
			break
	for i in res:
		print(solution(i))


