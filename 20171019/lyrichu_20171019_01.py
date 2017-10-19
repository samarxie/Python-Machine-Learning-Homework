# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
现在有一个m*n的网格(m,n均小于100)，现在在左上角有一个点A，右下角有一个点B，规定点A每次只能往右或者往下移动，问从A移动到B一共有多少种不同
的方法？
'''
from functools import reduce

def product(n):
    '''
    计算 n的阶乘
    :param n: 数字n
    :return: n!
    '''
    if(n == 0):
        return 1
    else:
        return reduce(lambda x,y:x*y,range(1,n+1))

def move_count(m,n):
    '''
    计算移动方法数
    :param m: m行
    :param n: n列
    :return: 移动总方法数
    '''
    # 一共需要向右移动n-1次，向下移动m-1次，所以总方法数为从m+n-2个位置中选出m-1个位置向下移动，其余的位置向右移动
    # 共有 C(m+n-2,m-1) = (m+n-2)!/((m-1)!*(n-1)!)
    return int(product(m+n-2)/(product(m-1)*product(n-1)))

def move_count_by_recursion(m,n):
    if(m == 1 or n == 1):
        return 1
    else:
        return move_count_by_recursion(m-1,n) + move_count_by_recursion(m,n-1)

if __name__ == '__main__':
    print("请输入m,n(使用逗号分隔):")
    m,n = map(int,input().split(","))
    print(move_count(m,n))
    print(move_count_by_recursion(m,n))
