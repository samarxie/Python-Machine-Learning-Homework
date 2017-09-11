#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/9 20:58
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170909_02.py
'''
@Description:
Q2:(背包问题)
现在有一个背包重量为n千克,有m种水果，每种水果的的重量分别为w1，w2,...,wm,价值为p1,p2,...,pm,
现在要使背包中所装的水果总价值最大，且总重量不超过水果的总负荷，问应该如何装水果？(这里假设m,n,w1,...,wm,p1,...,pm 均为正整数)
输入:
n,m
w1,w2,...,wm
p1,p2,...,pm
输出:
装入水果序号
总重量,总价值
例:
输入：
4,2
1,2
10,22
输出:
2,2
4,44
'''
# 本题可以使用贪婪算法，基本的思想是先装性价比高的水果,性价比这里是指 价值/重量
# 当问题规模较大时，贪婪算法只能给出近似解，可以用遗传算法等搜索算法求出更优解
# 但是对于一般的情况，由于背包问题是NP完全问题，所以无法给出其一般的最优解，一般求出
# 的是近似最优解

n,m = map(lambda x:int(x),raw_input().split(","))
w_list = map(lambda x:int(x),raw_input().split(",")) # 水果重量列表
p_list = map(lambda x:int(x),raw_input().split(",")) # 水果价格列表
k_list = [float(p_list[i])/w_list[i] for i in range(m)] #性价比列表
index_k_list = [(i,k_list[i]) for i in range(m)] # (水果序号,性价比) 列表
index_k_list.sort(key= lambda x:x[1],reverse=True) # 按照性价比递减排序
weight = 0 # 背包初始装入水果重量
price = 0 # 装入水果价值
sort = 1 # 已经装入的水果种类
index = index_k_list[sort-1][0] # 目前装入哪个水果(序号)，初始化为性价比最高的水果
while(weight < n):
    weight += w_list[index]
    # 如果装入水果超重
    if(weight > n):
        weight -= w_list[index]
        if(min(w_list) <= n-weight):
            sort += 1
            index = index_k_list[sort-1][0]
        else:
            break
    else:
        price += p_list[index]

print(str(weight) + "," + str(price))
