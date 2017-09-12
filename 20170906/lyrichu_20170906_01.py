#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# @Time   : 2017/9/6 8:45
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170906_02.py
'''
@Description:输出小于等于N的所有素数
'''
from math import sqrt
# isPrime(n) 用于判断n是否为素数,是素数返回True,不是返回False
def isPrime(n):
	if(n==2 or n==3):
		return True
	else:
		for i in range(2,int(sqrt(n))+1):
			if(n % i == 0):
				return False
		return True
num = int(raw_input()) # N
res = "" # 存放结果的字符串
for i in range(2,num+1):
	if(isPrime(i)):  
		if(i < num):
			res += (str(i) + " ")
		else:
			res += str(i)
	else:
		continue
print(res)
