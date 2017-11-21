#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170928_02.py
@time: 2017/9/28 10:49
@description:扑克牌的24点游戏是一个大家广为熟知的游戏。现在每次随机地从1-13中取出四个数字(可以重复)，问在每个数字都需要使用且只能使用一次，数字
运算只能使用加减乘除中的一种的条件下，如何操作才能得到数字24？如果存在解，则返回具体的操作方法(全部的解)，如果不存在则返回0。例如:
输入：2 3 4 5
输出:
2*(3+4+5) = 24
"""
from copy import deepcopy
def points24(numbersList):
    '''
    计算24点
    :param numbersList: 数字列表
    :return: 所有可能的组合
    '''
    plus = "+"
    minus = "-"
    multi = "x"
    divide = "/"
    # 如果只有两个数字
    if(len(numbersList) == 2):
        return [[numbersList[0],plus,numbersList[1]],[numbersList[0],minus,numbersList[1]],
                [numbersList[1],minus,numbersList[0]],[numbersList[0],multi,numbersList[1]],
                [numbersList[0],divide,numbersList[1]],[numbersList[1],divide,numbersList[0]]]
    # 如果有3个数字
    elif(len(numbersList) == 3):
        resList = []
        for i in range(3):
            # 去除一个数字
            restNumber = deepcopy(numbersList)
            restNumber.pop(i)
            for v in points24(restNumber):
                resList.extend(points24([v,numbersList[i]]))
        return resList
    # 如果有四个数字
    else:
        resList = []
        # 第一种情况，一个数字与三个数字结果组合
        for i in range(4):
            # 去除一个数字
            restNumber = deepcopy(numbersList)
            restNumber.pop(i)
            for v in points24(restNumber):
                resList.extend(points24([v,numbersList[i]]))
        # 第二种情况，两个数字的结果与两个数字的结果进行组合
        for i in range(3):
            for j in range(i+1,4):
                exp1 = [numbersList[i],numbersList[j]]
                exp2 = deepcopy(numbersList)
                exp2.pop(i)
                exp2.pop(j-1)
                for u in points24(exp1):
                    for v in points24(exp2):
                        resList.extend(points24([u,v]))
        return resList


def computeExression(expression):
    '''
    计算表达式的值
    :param expression: 表达式(嵌套列表)
    :return: 表达式的值
    '''
    # 如果第一个元素是一个列表
    # 则将其转换为数字
    if(isinstance(expression[0],list)):
        num1 = computeExression(expression[0])
    else:
        num1 = expression[0]
    if(isinstance(expression[2],list)):
        num2 = computeExression(expression[2])
    else:
        num2 = expression[2]
    if(expression[1] == '+'):
        return num1 + num2
    elif(expression[1] == '-'):
        return num1 - num2
    elif(expression[1] == 'x'):
        return num1*num2
    else:
        # 如果分母为0
        if(float(num2) == 0.):
            # 返回无穷大
            return float('inf')
        else:
            return float(num1)/num2



def prettyPrint(expression):
    '''
    将表达式美观打印出来
    :param expression: 表达式(嵌套列表)
    :return: 美观打印字符串
    '''
    resStr = ''
    if(isinstance(expression[0],list)):
        Str1 = '(' + prettyPrint(expression[0]) + ')'
    else:
        Str1 = str(expression[0])
    if(isinstance(expression[2],list)):
        Str2 = '(' + prettyPrint(expression[2]) + ')'
    else:
        Str2 = str(expression[2])
    return Str1 + expression[1] + Str2




if __name__ == '__main__':
    numbersList = list(map(lambda x:int(x),input().split(" ")))
    resList = points24(numbersList)
    # index 统计解的个数
    index = 0
    # 统计不重复的结果
    setList = []
    for res in resList:
        if(float(computeExression(res)) == 24.):
            # 如果结果未出现过
            if(res not in setList):
                print(prettyPrint(res) + ' = 24')
                index += 1
                setList.append(res)
        else:
            continue
    # 如果无解
    if(index == 0):
        print(0)










