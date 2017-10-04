#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence
@contact: 919987476@qq.com
@software: PyCharm
@file: test12.py
@time: 2017/10/3 10:39
@description:
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，差最小的有多少对呢？差最大呢？
输入描述:
 输入包含多组测试数据。
 对于每组测试数据：
 N - 本组测试数据有n个数
 a1,a2...an - 需要计算的数据
 保证:
 1<=N<=100000,0<=ai<=INT_MAX.
输出描述:
对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。
输入例子1:
6
45 12 45 32 5 6
输出例子1:
1 2
"""
from collections import Counter

def computeMinMax(numList,count):
    '''
    计算差最小的对数与差最大的对数
    :param numList: 输入数字列表
    :return: (差最小对数，最大对数)
    '''
    if(count == 1):
        return (0,0)
    else:
        if(count == 2):
            return (1,1)
        else:
            # 最小数
            Min = min(numList)
            # 最大数
            Max = max(numList)
            # 如果最小值和最大值相等
            if(Min == Max):
                return (int(count*(count-1)/2),int(count*(count-1)/2))
            # 如果最小值和最大值不等
            else:
                counter = Counter(numList)
                # 统计每个数字出现次数
                values = list(counter.values())
                # 每个数字都只出现一次
                if(max(values) == 1):
                    return (1,1)
                else:
                    # 遍历每个数字出现次数列表
                    # 统计差为0的个数即为差值最小对数
                    minCount = 0
                    # 差值最大对数即为最大值与最小值只差对数
                    maxCount = counter[Max]*counter[Min]
                    for v in values:
                        if(v > 1):
                            minCount += int(v*(v-1)/2)
                    return (minCount,maxCount)


if __name__ == '__main__':
    count = int(input())
    numList = list(map(lambda x:int(x),input().split(" ")))
    mimCount,maxCount = computeMinMax(numList,count)
    print(str(mimCount)+" "+str(maxCount))



