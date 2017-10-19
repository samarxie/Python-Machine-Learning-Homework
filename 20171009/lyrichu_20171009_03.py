#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20171009_03.py
@time: 2017/10/9 13:22
@description:Q3：现在有一堆(25张)已经被分割的RGB图片(参见压缩包)，试设计一种算法将这些图片复原拼接为原本的完整图片。
"""
import numpy as np
from PIL import Image
import random

def calculateOneImage(imgArr,x,y,xMax,yMax):
    '''
    计算单张图片与周围图片的差异度
    :param imgArr:图像数组,shape:(xMax,yMax,d,h,3)
    :param x: 行索引
    :param y: 列索引
    :param xMax:行最大值
    :param yMax:列最大值
    :return: 差异度大小
    '''
    dis = 0
    if(y-1 >= 0):
        dis += np.sum(np.abs(imgArr[x][y][:,0]-imgArr[x][y-1][:,-1]))
    if(y+1 < yMax):
        dis += np.sum(np.abs(imgArr[x][y][:,-1]-imgArr[x][y+1][:,0]))
    if(x-1 >= 0):
        dis += np.sum(np.abs(imgArr[x][y][0,:]-imgArr[x-1][y][-1,:]))
    if(x+1 < xMax):
        dis += np.sum(np.abs(imgArr[x][y][-1,:]-imgArr[x+1][y][0,:]))

    return dis

def calculateAllImages(imgArr):
    '''
    计算某一种组合的全部图像差异度之和
    :param imgArr: 全体图像数组
    :return: 差异度之和
    '''
    # 初始化差异度之和
    allDis = 0
    xMax,yMax,_,_,_ = imgArr.shape
    for i in range(xMax):
        for j in range(yMax):
            allDis += calculateOneImage(imgArr,i,j,xMax,yMax)
    return allDis

def getImagesArrList(num,imgPath):
    '''
    按顺序得到imgArr列表
    :param num: 列表长度
    :param imgPath: 图像文件夹路径
    :return: imgArrList
    '''
    imgArrList = []
    for i in range(1,num+1):
        path = imgPath + "%d.jpg" % i
        img = Image.open(path)
        arr = np.asarray(img,dtype=np.uint8)
        imgArrList.append(arr)

    return imgArrList

def convertIndexListToImgArr(indexList,imgArrList,width,height,xMax,yMax):
    '''
    将图片排序列表转化为图像数组(5维)
    :param imgPath:图像文件夹路径
    :param indexList: 排序列表
    :param imgArrList:imgArr列表
    :param width: 单个图像宽度
    :param height: 单个图像高度
    :param xMax: 行最大值
    :param yMax: 列最大值
    :return: imgArr
    '''
    imgArr = np.zeros((xMax,yMax,height,width,3))
    indexPair = [(i,j) for i in range(5) for j in range(5)]
    for i in range(len(indexList)):
        # 行数和列数
        x,y = indexPair[i]
        imgArr[x][y] = imgArrList[indexList[i]-1]

    return imgArr


def showFullImage(imgArr):
    '''
    显示拼接之后的完整图像
    :param imgArr: 高维图像数组
    :return: None
    '''
    xMax,yMax,height,width,_ = imgArr.shape
    # 初始化完整图像数组
    fullImgArr = np.zeros((width*yMax,height*xMax,3),dtype=np.uint8)
    for i in range(xMax):
        for j in range(yMax):
            x0 = i*height
            x1 = (i+1)*height
            y0 = j*width
            y1 = (j+1)*width
            fullImgArr[x0:x1,y0:y1] = imgArr[i][j]

    fullImg = Image.fromarray(fullImgArr,mode="RGB")
    fullImg.show()


def disturb(indexList):
    '''
    随机打乱一个序号数组生成一个新的解
    :param indexList:
    :return: 打乱序号之后的数组
    '''
    num = len(indexList)
    pos1 = random.choice(range(num))
    pos2 = random.choice(range(num))
    disturbIndexList = [i for i in indexList]
    disturbIndexList[pos1],disturbIndexList[pos2] = disturbIndexList[pos2],disturbIndexList[pos1]
    return disturbIndexList


def solve(num,imgPath,width,height,xMax,yMax,tStart=100,tEnd=1e-6,q=0.9,L=100):
    '''
    使用模拟退火算法(SA)求解差异度之和的最小值(近似值,问题为TSP问题,是NP问题，大规模求解只能得到近似解)
    :param num: indexList 长度
    :param imgPath:图像文件夹路径
    :param width:单个图像宽度
    :param height:单个图像高度
    :param xMax:行最大值
    :param yMax:列最大值
    :param tStart: 初始温度，默认为100
    :param tEnd: 结束温度，默认为1e-6
    :param q: 退火系数，默认为0.9
    :param L: 每个温度时的迭代次数，即链长,默认为100
    :return: 差异度最小的排序组合
    '''
    # 初始化
    initIndexList = [i for i in range(1,num+1)]
    # 随机打乱
    random.shuffle(initIndexList)
    # 初始温度
    t = tStart
    imgArrList = getImagesArrList(num,imgPath)
    while(t >= tEnd):
        for i in range(L):
            # 扰动初始解
            disturbIndexList = disturb(initIndexList)
            initImgArr = convertIndexListToImgArr(initIndexList,imgArrList,width,height,xMax,yMax)
            disturbImgArr = convertIndexListToImgArr(disturbIndexList,imgArrList,width,height,xMax,yMax)
            # 计算相似度之和的差
            delta = (calculateAllImages(disturbImgArr) - calculateAllImages(initImgArr))/(10**2)
            # print(delta)
            if(delta < 0):
                initIndexList = disturbIndexList
            else:
                rnd = np.exp(-delta/t)
                # 以一个非常小的概率接受恶化解
                if(random.random() < rnd):
                    initIndexList = disturbIndexList
        t *= q
        initImgArr = convertIndexListToImgArr(initIndexList,imgArrList,width,height,xMax,yMax)
        print(calculateAllImages(initImgArr))
    print("best indexList:",initIndexList)
    imgArr = convertIndexListToImgArr(initIndexList,imgArrList,width,height,xMax,yMax)
    print("best max sum:",calculateAllImages(imgArr))
    showFullImage(imgArr)


if __name__ == '__main__':
    imgPath = "Images/"
    width = height = 80
    xMax = yMax = 5
    num = xMax*yMax
    # indexList = [i for i in range(1,num+1)]
    # random.shuffle(indexList)
    # imgArrList = getImagesArrList(num,imgPath)
    # imgArr = convertIndexListToImgArr(indexList,imgArrList,width,height,xMax,yMax)
    # print(calculateAllImages(imgArr))
    tStart = 300
    tEnd = 100
    q = 0.99
    L = 100
    solve(num,imgPath,width,height,xMax,yMax,tStart,tEnd,q,L)









