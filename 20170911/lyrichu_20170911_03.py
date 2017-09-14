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

def solveBlocks(int_list):
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

# 考虑从石块高度最高处向两边一定是非增的(不严格递减)
# right = True 表示最高点在第一位，向右递减
# right = False 表示最高点在最后一位，向左递减
def new_solve(int_list,right = True):
    n = len(int_list)
    count = 0
    if(right):
        maxIndex = 0
        nowIndex = maxIndex + 1 # 当前序号
        while(nowIndex < n-1):
            while(nowIndex < n-1 and int_list[nowIndex] >= int_list[nowIndex+1]):
                nowIndex += 1
            if(nowIndex == n-1):
                return count
            else:
                nowIndex += 1
                high = int_list[nowIndex]
                for i in range(maxIndex+1,nowIndex):
                    if(int_list[i] < high):
                        count += (high-int_list[i])
                        int_list[i] = high
    else:
        maxIndex = n -1
        nowIndex = maxIndex -1
        while(nowIndex > 0):
            while(nowIndex >0 and int_list[nowIndex] >= int_list[nowIndex - 1]):
                nowIndex -= 1
            if(nowIndex == 0):
                return count
            else:
                nowIndex -= 1
                high = int_list[nowIndex]
                for i in range(nowIndex+1,maxIndex):
                    if(int_list[i] < high):
                        count += (high-int_list[i])
                        int_list[i] = high
    return count

# 求解一般的情况
def new_solveBlocks(int_list):
    n = len(int_list)
    maxIndex = int_list.index(max(int_list))
    if(maxIndex == 0):
        return new_solve(int_list,True)
    elif(maxIndex == n-1):
        return new_solve(int_list,False)
    else:
        left_list = int_list[:maxIndex+1]
        right_list = int_list[maxIndex:]
        return new_solve(left_list,False) + new_solve(right_list,True)

if __name__ == '__main__':
    int_list = map(lambda x:int(x),raw_input().split(" "))
    count1,res_list = solveBlocks(int_list)
    # 打印水块的数目
    print("解法一:")
    print("雨滴数量为 %d" % count1)
    # 打印实际的水块、方块的分布情况
    for v in res_list:
        print(" ".join(map(lambda x:str(x),v)))
    print("解法二:")
    count2 = new_solveBlocks(int_list)
    print("雨滴数量为 %d" % count2)



