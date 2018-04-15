#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @date    : 2018-04-15 09:14:18
# @author  : lyrichu
# @email   :919987476@qq.com
# @link    : https://www.github.com/Lyrichu
# @version : 0.1
# @description:
'''
给定一组数据,X=[[1,1],[2,3],[4,5],[5,7]],Y = [2,5,9,12]
使用随机梯度下降法(SGD)求y = w0 + w1*x1 + w2*x2 的最佳拟合系数
'''
import random

def solution(X,Y,lr,eps,max_iteration):
	# grad w0:2*(w0 + w1*x1 + w2*x2-y)
	# grad w1:2*(w0 + w1*x1 + w2*x2-y)*x1
	# grad w2:2*(w0 + w1*x1 + w2*x2-y)*x2
	# 随机选择一个数据点
	w0,w1,w2 = 0,0,0
	iteration = 0
	while True:
		xr,yr = random.choice(list(zip(X,Y)))
		loss = sum([(w0+w1*x1+w2*x2-y)**2 for (x1,x2),y in zip(X,Y)]) # 总平方损失函数
		print("iteration %d,loss = %.4f" %(iteration,loss))
		grad_w0 = 2*(w0+w1*xr[0]+w2*xr[1]-yr)
		grad_w1 = grad_w0*xr[0]
		grad_w2 = grad_w0*xr[1]
		# 如果梯度更新达到最小阈值或者超过迭代次数,则退出循环
		if max([lr*abs(grad_w0),lr*abs(grad_w1),lr*abs(grad_w2)]) < eps or iteration > max_iteration:
			break
		w0 -= lr*grad_w0
		w1 -= lr*grad_w1
		w2 -= lr*grad_w2
		iteration += 1
	return (w0,w1,w2)




if __name__ == '__main__':
	lr = 0.001 # 学习率
	eps = 0.0005 # 停止迭代的阈值
	max_iteration = 100
	X = [[1,1],[2,3],[4,5],[5,7]]
	Y = [2,5,9,12]
	w = solution(X,Y,lr,eps,max_iteration)
	print("w0:",w[0])
	print("w1:",w[1])
	print("w2:",w[2])