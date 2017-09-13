#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/13 9:25
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170913_02.py
'''
@Description:
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# 得到第n个丑数
def getUglyNumber(n):
    if(n == 1):
        return 1
    else:
        num = 2 # 初始数字
        index = 1 # 当前丑数的序号
        while(index < n):
            factor = num
            flag = True  # flag 用于判断当前数字是否是丑数
            while(factor>1):
                if(factor %2 == 0):
                    factor /= 2
                elif(factor % 3 == 0):
                    factor /= 3
                elif(factor % 5 == 0):
                    factor /= 5
                else:
                    flag = False
                    num += 1
                    break
            # 如果是丑数
            if(flag):
                index += 1
                num += 1
    return num-1

if __name__ == '__main__':
    n = int(raw_input())
    print(getUglyNumber(n))



