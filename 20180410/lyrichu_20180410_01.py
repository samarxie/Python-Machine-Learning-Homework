#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-04-10 16:20:49
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
Q1:逆波兰表达式(栈的应用)
输入输出实例:
输入:"2 1 + 3 *"
输出:((2+1)*3)=9
输入:"4 13 5 / +"
输出:(4+(13/5))=6
'''
def solution(s):
	stack1 = []
	stack2 = []
	for i in s:
		if i.isdigit(): # 数字
			stack1.append(i)
			stack2.append(i)
		else: # 操作符
			a1 = stack1.pop()
			b1 = stack1.pop()
			a2 = stack2.pop()
			b2 = stack2.pop()
			r1 = cal(b1,a1,i)
			stack1.append(r1) # 计算结果
			r2 = "(%s%s%s)" %(b2,i,a2)
			stack2.append(r2) # 表达式
	res = "%s=%s" %(stack2.pop(),stack1.pop())
	return res 

def cal(m,n,op):
	if op == '+':
		return str(int(m)+int(n))
	elif op == '-':
		return str(int(m)-int(n))
	elif op == '*':
		return str(int(m)*int(n))
	elif op == "/":
		return str(int(m)//int(n))

if __name__ == '__main__':
	s = input().split()
	res = solution(s)
	print(res)
