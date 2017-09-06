# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 18:57:35 2017

@author: zyy
"""

"zyy-20170906-01 小于等于N的素数"

"基本思路："
"在一般领域，对正整数n，如果用2到根号n之间的所有整数去除，均无法整除，则n为质数"

from math import sqrt

"定义一个函数判断一个数字是否是素数"
def ifprime(num):
    if num == 1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num%i == 0:
            return False
    return True
    
"再定义一个函数打印出小于N的素数" 
def PrintPrimes(N):
    for i in range(1,N):
        if ifprime(i) == True:
            print(i)
    
print("请输入N，得出小于N的素数") 
N = int(input("N = "))
PrintPrimes(N)
