#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Kimmyzhang
@Email: 902227553.com 
@File: kimmyzhang_20170913_03.py
@Time: 2017/9/14 16:34
"""

martix_demsion = 6
martix = [[1, 2, 3, 4,5,6]for i in range(6)]
print(martix)


def clockwisePrint(martix):
    temp1 = []
    temp2 = []
    times = divmod(martix_demsion, 2)[0]
    if  divmod(martix_demsion, 2)[1]== 0:
        for i in range(times):
            j = i
            while j < martix_demsion - i：
                if j == i :
                    temp1 = temp1 + martix[j][i : martix_demsion - i]
                elif j == (martix_demsion - i - 1):
                    # print(j)
                    temp = martix[martix_demsion - i - 1][i : martix_demsion - i]
                    temp.reverse()
                    temp1  = temp1 + temp
                    # print(temp1)
                else:
                    print(martix[j][0])
                    temp2 = temp2 + [martix[j][0]]
                    temp1 = temp1 + [martix[j][martix_demsion - 1]]

                j += 1
            temp2.reverse()
            temp1 = temp1 + temp2
            temp2 = []

    print(temp1 + temp2)
clockwisePrint(martix)
