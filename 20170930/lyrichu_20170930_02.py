#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170930_02.py
@time: 2017/10/1 17:31
@description:求解生命游戏(game of life,也被称为元胞自动机)。
该游戏1970年由英国数学家J. H. Conway所提出，某一细胞的邻居包
括上、下、左、右、左上、左下、右上与右下相邻之细胞，游戏规则如下：
孤单死亡：如果细胞的邻居小于一个，则该细胞在下一次状态将死亡。
拥挤死亡：如果细胞的邻居在四个以上，则该细胞在下一次状态将死亡。
稳定：如果细胞的邻居为二个或三个，则下一次状态为稳定存活。
复活：如果某位置原无细胞存活，而该位置的邻居为三个，则该位置将复活一细胞。
利用上述简单的规则可以得到很多复杂的行为，比如模拟交通堵塞，发生火灾等等。
试查找相关资料，利用元胞自动机模拟一些有趣的现象。
"""
import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
import numpy as np

LIVE = 255 # 白色表示存活
DEATH = 0 # 黑色表示死亡
BLANK = np.array([255,255,255],dtype=np.uint8) # 空白位置(白色)
TREE = np.array([0,255,0],dtype=np.uint8) # 树木(绿色)
FIRE = np.array([255,0,0],dtype=np.uint8) # 着火(红色)

def getNeighbors(m,n,width,height,array):
    '''
    得到(m,n)位置邻居数目
    :param m: 横坐标
    :param n: 纵坐标
    :param width: 图像宽
    :param height: 图像高
    :param array: 图像数组
    :return: (m,n)位置邻居数目
    '''
    # 初始化邻居数目
    count = 0
    for i in range(m-1,n+2):
        for j in range(n-1,n+2):
            if(i >=0 and i < height and j >=0 and j < width):
                if(i != m and j != n and array[i][j] == LIVE):
                    count += 1
    return count

def initArray(width,height,initMethod = 0,r = 0.95):
    '''
    产生初始化数组
    :param width:图像宽
    :param height:图像高
    :param initMethod:使用的初始化方法(0,1...代表不同的方法)
    :param r: 方法1 阈值大小
    :return:array
    '''
    array = np.zeros((width,height),dtype=np.uint8)
    # 采用随机初始化的方式
    if(initMethod == 0):
        for i in range(height):
            for j in range(width):
                rand = np.random.random()
                if(rand < r):
                    array[i][j] = LIVE
    # 只将中心点3*3位置置为LIVE
    elif(initMethod == 1):
        centerX = height/2
        centerY = width/2
        for i in range(centerX-1,centerX+2):
            for j in range(centerY-1,centerY+2):
                array[i][j] = LIVE
    else:
        pass
    return array

def initForestArray(width,height,init_trees_rand = 0.5):
    '''
    初始化森林
    :param width:图像宽
    :param height: 图像高
    :param init_trees_rand: 产生树木阈值
    :return: 初始化之后的森林
    '''
    # 初始化森林
    forestArray = np.zeros((width,height,3),dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            # 大于阈值，为树木
            if(np.random.random() < init_trees_rand):
                forestArray[i][j] = TREE
            else:
                forestArray[i][j] = BLANK
    return forestArray

def update(array,index,statusArray,reactionArray,forestStatusArray,fire_rand = 0.0001,grow_tree_rand=0.001,updateMethod=0,statusEpsilon=0.6):
    '''
    更新图像数组
    :param array: 图像数组
    :param index:更新次数
    :param updateMethod: 更新方式
    :param statusEpsilon: 方法2 更新阈值
    :param reactionArray:激发状态数组
    :param forestStatusArray:森林着火状态数组
    :param fire_rand:树木着火概率
    :param grow_tree_rand:空位长出树木概率
    :return: None
    '''
    if(updateMethod == 4):
        width,height,_ = array.shape
    else:
        width,height = array.shape
    for i in range(height):
        for j in range(width):
            if(updateMethod != 4):
                # 计算邻居个数
                neighbors = getNeighbors(i,j,width,height,array)
            # conway 生命机
            if(updateMethod == 0):
                # 如果邻居个数为3，则变为LIVE
                if(neighbors == 3):
                    array[i][j] = LIVE
                # 如果邻居个数为2，则保持不变
                elif(neighbors == 2):
                    continue
                # 否则变为死亡
                else:
                    array[i][j] = DEATH
            # 表面张力更新
            elif(updateMethod == 1):
                if(neighbors < 4 or neighbors == 5):
                    array[i][j] = DEATH
                else:
                    array[i][j] = LIVE
            elif(updateMethod == 2):
                # 产生一个随机数
                r = np.random.random()
                # 如果有邻居
                if(neighbors >0):
                    statusArray[i][j] = 1
                if((neighbors >0 and r > statusEpsilon ) or statusArray[i][j] == 0):
                    array[i][j] = LIVE
            # 激发介质方法
            # 状态0 是休眠期，状态 1-5为活跃状态，6-9是极活跃状态
            elif(updateMethod == 3):
                # 如果细胞处于活跃状态且邻居数目大于等于3
                # 则变为LIVE
                if(reactionArray[i][j] > 0 and reactionArray[i][j] <=5 and neighbors >=3):
                    array[i][j] = LIVE
                # 如果当前状态在1-8之间，则状态向前进1
                if(reactionArray[i][j] > 0 and reactionArray[i][j] < 9):
                    reactionArray[i][j] += 1
                # 如果当前状态是9，则下一次状态是0(进入休眠期)
                if(reactionArray[i][j] == 9):
                    reactionArray[i][j] = 0
            # 模拟森林着火
            # 状态BLANK是空位，TREE是树木，FIRE是着火
            elif(updateMethod == 4):
                # 四个邻居着火数目
                neighborsFireNum = 0
                if(i-1 >= 0 and (forestStatusArray[i-1][j] == FIRE).all()):
                    neighborsFireNum += 1
                if(j-1 >= 0 and (forestStatusArray[i][j-1] == FIRE).all()):
                    neighborsFireNum += 1
                if(j+1 < width and (forestStatusArray[i][j+1] == FIRE).all()):
                    neighborsFireNum += 1
                if(i+1 < height and (forestStatusArray[i+1][j] == FIRE).all()):
                    neighborsFireNum += 1
                # 如果当前位置是树木且周围有邻居着火
                # 则该位置也着火
                if((forestStatusArray[i][j] == TREE).all() and neighborsFireNum > 0):
                    forestStatusArray[i][j] = FIRE
                # 燃烧的位置下一个时刻为空
                if((forestStatusArray[i][j] == FIRE).all()):
                    forestStatusArray[i][j] = BLANK
                # 树木以一个极小概率着火
                if(np.random.random() <= fire_rand and (forestStatusArray[i][j] == TREE).all()):
                    forestStatusArray[i][j] = FIRE
                # 空位以一个极小概率长出树木
                if(np.random.random() < grow_tree_rand and (forestStatusArray[i][j] == BLANK).all()):
                    forestStatusArray[i][j] = TREE
            # 气体动力学仿真
            elif(updateMethod == 5):
                if(index % 2 == 1):
                    # 右下4元胞为邻居关系
                    if(i+1 < height and j+1 <width):
                        # 交换对角元胞
                        array[i][j],array[i+1][j+1] = array[i+1][j+1],array[i][j]
                        array[i+1][j],array[i][j+1] = array[i][j+1],array[i+1][j]
                        if(array[i+1][j+1] == LIVE and array[i][j] ==LIVE and array[i+1][j] == DEATH and array[i][j+1] == DEATH):
                            array[i+1][j+1] = DEATH
                            array[i][j] = DEATH
                            array[i+1][j] = LIVE
                            array[i][j+1] = LIVE
                        if(array[i+1][j+1]==DEATH and array[i][j] == DEATH and array[i+1][j] == LIVE and array[i][j+1] == LIVE):
                            array[i+1][j+1] = LIVE
                            array[i][j] = LIVE
                            array[i+1][j] = DEATH
                            array[i][j+1] = DEATH
                else:
                    # 左上4元胞为邻居关系
                    if(i-1 >=0 and j-1 >= 0):
                        # 交换对角元胞
                        array[i][j],array[i-1][j-1] = array[i-1][j-1],array[i][j]
                        array[i-1][j],array[i][j-1] = array[i][j-1],array[i-1][j]
                        if(array[i-1][j-1] == LIVE and array[i][j] ==LIVE and array[i-1][j] == DEATH and array[i][j-1] == DEATH):
                            array[i-1][j-1] = DEATH
                            array[i][j] = DEATH
                            array[i-1][j] = LIVE
                            array[i][j-1] = LIVE
                        if(array[i-1][j-1]==DEATH and array[i][j] == DEATH and array[i-1][j] == LIVE and array[i][j-1] == LIVE):
                            array[i-1][j-1] = LIVE
                            array[i][j] = LIVE
                            array[i-1][j] = DEATH
                            array[i][j-1] = DEATH
                # 处理碰壁的情况
                if(i-1 >=0 and i+1 < height and array[i][j] == LIVE):
                    if(j-1 < 0):
                        array[i][j] = DEATH
                        # 粒子反弹
                        array[i][j+1] = LIVE
                    elif(j+1 >= width):
                        array[i][j] = DEATH
                        array[i][j-1] = LIVE
                else:
                    if(j-1 > 0 and j+1 < width and array[i][j] == LIVE):
                        if(i-1 < 0):
                            array[i][j] = DEATH
                            array[i+1][j] = LIVE
                        elif(i+1 >= height):
                            array[i][j] = DEATH
                            array[i-1][j] = LIVE
                    if(i-1 < 0 and j-1 < 0 and array[i][j] == LIVE):
                        array[i][j] = DEATH
                        array[i+1][j+1] = LIVE
                    elif(i+1 >=height and j-1<0 and array[i][j] == LIVE):
                        array[i][j] = DEATH
                        array[i-1][j+1] = LIVE
                    elif(i+1 >=height and j+1 >=width and array[i][j] == LIVE):
                        array[i][j] = DEATH
                        array[i-1][j-1] = LIVE
                    elif(i-1 <0 and j+1>=width and array[i][j] == LIVE):
                        array[i][j] = DEATH
                        array[i+1][j-1] = LIVE
            # 堆沙规则
            elif(updateMethod == 6):
                if(i+1 < height):
                    if(array[i+1][j] == DEATH and array[i][j] == LIVE):
                        array[i+1][j] = LIVE
                        array[i][j] = DEATH
                    if(j+1 < width and array[i][j] == LIVE and array[i+1][j] == LIVE and array[i][j+1] == DEATH and array[i+1][j+1] == DEATH):
                        array[i][j],array[i+1][j+1] = DEATH,LIVE
                    if(j+1 < width and array[i][j] == DEATH and array[i+1][j] == DEATH and array[i][j+1] == LIVE and array[i+1][j+1] == LIVE):
                        array[i][j+1],array[i+1][j] = DEATH,LIVE






def gameOfLife(width=50,height=50,num=100,r = 0.95,fire_rand = 0.0001,grow_tree_rand = 0.01,init_trees_rand = 0.5,initMethod = 0,updateMethod = 0,statusEpsilon = 0.6):
    '''
    game of life
    :param width: 显示宽度
    :param height: 显示高度
    :param num: 迭代次数
    :param r: 初始化方法1阈值
    :param fire_rand:模拟某一个树木着火的概率(一个非常小的值)
    :param grow_tree_rand:模拟森林着火，空位长出树木的概率(一个很小的值)
    :param initMethod:初始化方法
    :param updateMethod:更新方法
    :param statusEpsilon: 方法2更新阈值
    :return: None
    '''
    plt.ion()
    # 初始化
    array = initArray(width,height,initMethod,r)
    # 方法2(渗流集群)的状态数组，记录每一个元素之前是否有过邻居
    # 0表示没有邻居，1表示有邻居
    statusArray = np.zeros((width,height))
    # 初始化激发状态数组(方法3激发介质用到)
    reactionArray = np.random.randint(0,10,size=(width,height))
    # 模拟森林着火初始状态数组
    # 状态BLANK是空位，TREE是树木，FIRE是着火
    forestStatusArray = initForestArray(width,height,init_trees_rand)
    for i in range(height):
        for j in range(width):
            # 着火
            if(np.random.random() <= fire_rand and (forestStatusArray[i][j] == TREE).all()):
                forestStatusArray[i][j] = FIRE
    # 如果是模拟森林着火
    if(updateMethod == 4):
        array = forestStatusArray
        plt.imshow(array)
    else:
        plt.imshow(array,cmap='gray')
    plt.title("image 1")
    index = 1
    while(index < num):
        # 更新数组
        update(array,index,statusArray,reactionArray,forestStatusArray,fire_rand,grow_tree_rand,updateMethod,statusEpsilon)
        # 如果是森林着火
        if(updateMethod == 4):
            plt.imshow(array)
        else:
            plt.imshow(array,cmap='gray')
        index += 1
        plt.title("image %d" % index)
        plt.pause(0.001)
    plt.show()


if __name__ == '__main__':
    # 图像宽度
    width = 120
    # 图像高度
    height = 120
    # 模拟次数
    num = 50
    # 选择的初始化方法
    initMethod = 0
    # 初始为LIVE的点所占比例
    r = 0.05
    # 着火概率
    fire_rand = 0.05
    # 空白位置长出树木的概率
    grow_tree_rand = 0.05
    # 初始化森林(森林所占比例)
    init_trees_rand = 0.99
    # 更新方式(0-6)
    updateMethod = 4
    # 方法2更新阈值
    statusEpsilon = 0.6
    # 启动生命游戏
    gameOfLife(width,height,num,r,fire_rand,grow_tree_rand,init_trees_rand,initMethod,updateMethod,statusEpsilon)







