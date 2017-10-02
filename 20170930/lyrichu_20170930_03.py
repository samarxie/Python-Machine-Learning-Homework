#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170930_03.py
@time: 2017/10/2 10:58
@description:一般而言，计算机所能存储的整数大小是有限制的，比如对于64位系统，C语言可以表示的最大整数的范围是(long long) -2^63 ~ 2^63-1。如果
还需要运算更大的数字，则需要考虑大数运算了。python 的 decimal 模块可以支持大数运算(包括整数与浮点数)，试查阅相关资料设计一个算法，可以
支持任意位整数的乘法(注意python本身就支持大整数乘法,请自己设计函数实现，不要直接使用内置的大数乘法)。
"""
def multi(numStr,char,index):
    '''
    计算某一个数字与某一位数字相乘的结果
    :param numStr: 一个大数
    :param char: 一位数字
    :param index: 该数字位于原数字末尾第几位(0开始)
    :return: 计算结果(字符串表示)
    '''
    # 初始化结果字符串
    resStr = ""
    # 数字位数
    digits = len(numStr)
    # 初始化下一位要相加的数字
    addNum = 0
    for i in range(digits):
        # 两个数字相乘的中间结果
        tempNum = int(char)*int(numStr[digits-1-i]) + addNum
        if(tempNum >= 10):
            # 当前位数字
            nowNum = tempNum % 10
            # 下一位要加的数字
            addNum = int(tempNum/10)
        else:
            nowNum = tempNum
            addNum = 0
        resStr = str(nowNum) + resStr
    if(addNum != 0):
        resStr = str(addNum) + resStr
    # 最后需要根据index补0
    resStr += "0"*index
    return resStr

def plusMultiStr(multiList):
    '''
    将按位相乘的结果相加
    :param multiList:
    :return: 相加之后的结果(字符串)
    '''
    # 要相加的数字个数
    num = len(multiList)
    # 所有要相加的数字中的最大数字位数
    maxDigits = max(map(lambda x:len(x),multiList))
    for i in range(num):
        # 前导补0，与最大数字位对齐
        multiList[i] = "0"*(maxDigits-len(multiList[i])) + multiList[i]
    # 初始化结果字符串
    resStr = ""
    # 初始化下一位要加的数字
    addNum = 0
    for i in range(maxDigits):
        tempNum = 0
        for j in range(num):
            tempNum += int(multiList[j][maxDigits-1-i])
        tempNum += addNum
        if(tempNum >=10):
            nowNum = tempNum % 10
            addNum = int(tempNum/10)
        else:
            nowNum = tempNum
            addNum = 0
        resStr = str(nowNum) + resStr
    return resStr


def simpleBigNumMultiply(num1,num2):
    '''
    简单的按位相乘法处理大数相乘
    :param num1: 第一个大整数
    :param num2: 第二个大整数
    :return: num1*num2(字符串表示)
    '''
    # 将数字变为字符串
    num1Str = str(num1)
    num2Str = str(num2)
    # 如果第一个数字位数小于第二个数字位数，则交换
    if(len(num1Str) < len(num2Str)):
        num1Str,num2Str = num2Str,num1Str
    # 计算数字位数
    num2Digits = len(num2Str)
    # 存放按位相乘以后的结果(字符串)
    multiList = []
    for i in range(num2Digits):
        # 得到按位相乘以后的字符串
        multiStr = multi(num1Str,num2Str[num2Digits-1-i],i)
        multiList.append(multiStr)
    # 将所有按位相乘的结果相加，得到最终计算结果(字符串)
    finalRes = plusMultiStr(multiList)
    return finalRes

def test():
    '''
    测试函数
    :return:
    '''
    # 测试 multi函数
    print(multi("1234","9",0)==str(1234*9))
    print(multi("1234","9",2)==str(1234*9)+"00")
    # 测试plusMultiStr函数
    print(plusMultiStr(["123","4560"]) == "4683")
    print(plusMultiStr(["132","2000","43210"]) == "45342")
    print(plusMultiStr(["6170","12340","246800"]) == str(1234*215))
    # 测试 simpleBigNumMultiply函数
    print(simpleBigNumMultiply("1234","215") == str(1234*215))
    print(simpleBigNumMultiply("12345678","234435689") == str(12345678*234435689))
    print(simpleBigNumMultiply("123456789101112122345786","22767456735478254682") == str(123456789101112122345786*22767456735478254682))

if __name__ == '__main__':
    # test()
    num1 = input("请输入第一个数字:")
    num2 = input("请输入第二个数字:")
    res = simpleBigNumMultiply(num1,num2)
    print("%s*%s=%s" %(num1,num2,res))




