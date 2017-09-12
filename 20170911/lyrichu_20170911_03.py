#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/11 13:49
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170911_03.py
'''
@Description:
'''
# 得到某一列方块或者水珠的高度
def getLen(lists):
    return sum([1 for i in lists if i >=0])

def solveBlocks():
    int_list = map(lambda x:int(x),raw_input().split(" "))
    n = len(int_list)
    max_len = max(int_list) # 方块最大高度
    xy_pos = [[-1 for i in range(max_len)] for j in range(n)] # 初始化储存(按列来储存)
    # 用 'b'表示当前位置填充的是方块，'o'表示填充的是水,' '表示为空
    # 初始化填充
    # 首先假设将所有可以填充的位置，如果没有方块，则填充水珠
    # 后面再根据一定的规则，将不合理位置的水珠移去
    for i in range(n):
        if(int_list[i] == 0):
            for j in range(max_len):
                xy_pos[i][j] = 'o'
        else:
            for j in range(max_len):
                xy_pos[i][j] = 'b' if j < int_list[i] else 'o'

    for i in range(n):
        for j in range(max_len):
            # 如果是第0列或者第n-1列
            # 一定无法放水珠,将该列所有水珠移除
            if(i == 0 or i == n-1):
                xy_pos[i][j] = ' ' if xy_pos[i][j] == 'o' else 'b'
            else:
                if(xy_pos[i][max_len-1-j] == 'b'): # 如果原来是方块
                    break
                else:
                    pos_x_left = i # 初始左横坐标
                    pos_x_right = i # 初始右横坐标
                    while((pos_x_left > 0 and xy_pos[pos_x_left-1][max_len-1-j] != 'b') or (pos_x_right < n-1 and xy_pos[pos_x_right+1][max_len-1-j] != 'b')):
                        if(pos_x_left > 0 and xy_pos[pos_x_left-1][max_len-1-j] != 'b'):
                            pos_x_left -= 1
                        if(pos_x_right < n-1 and xy_pos[pos_x_right+1][max_len-1-j] != 'b'):
                            pos_x_right += 1
                    if(pos_x_left <= 0 or pos_x_right >= n-1):
                        xy_pos[i][max_len-1-j] = ' ' # 空
                    else:
                        xy_pos[i][max_len-1-j] = 'o' # 水
    count = 0 # 计数
    for v in xy_pos:
        for i in range(max_len):
            if(v[i] == 'o'):
                count += 1
    res_list = [[v[max_len-1-i] for v in xy_pos] for i in range(max_len)]
    return count,res_list

if __name__ == '__main__':
    count,res_list = solveBlocks()
    # 打印水块的数目
    print(count)
    # 打印实际的水块、方块的分布情况
    for v in res_list:
        print(" ".join(map(lambda x:str(x),v)))
