# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:12:49 2017

@author: zyy
"""

"zyy-20170906-02 前N项斐波那契数列"
"基本思路：斐波那契数列前两项是1，1；接下来项是前两项的和"

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
print("请输入N，得出前N项斐波那契数列")      
N = int(input("N = "))
for i in fib(N):
    print(i)