#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170929_03.py
@time: 2017/9/29 14:11
@description:多层神经网络的一种核心算法之一就是BP算法(误差反向传播算法)，阅读相关资料，实现基础的BP算法，并用数据检验其效果如何。
"""
import numpy as np

def sigmoid(arr):
    '''
    sigmoid 函数
    :param arr: 输入向量
    :return: 向量转换之后的值
    '''
    return 1./(1 + np.exp(-arr))

def mse(y,predict_y):
    '''
    计算均方误差
    :param y: 实际值
    :param predict_y: 预测值
    :return: 均方误差
    '''
    return np.sqrt((np.mean((y-predict_y)**2)))

def calculate(x,outputNum,hidden_layers_num,inputWeights,outputWeights,gamaBias,thetaBias):
    '''
    给定神经网络参数以及输入值，计算预测的输出值
    :param x: 输入数据
    :param output_num: 输出层节点数
    :param hidden_layers_num: 隐藏层数
    :param inputWeights: 输入权重
    :param outputWeights: 输出权重
    :param gamaBias: 输入 bias
    :param thetaBias: 输出bias
    :return: 预测值
    '''
    # 样本总数
    dataNum = x.shape[0]
    # 初始化预测值
    predict_y = np.zeros((dataNum,outputNum))
    for i in range(dataNum):
        # 初始化隐藏层节点的值
        hidden_values = np.zeros(hidden_layers_num)
        for j in range(hidden_layers_num):
            hidden_values[j] = np.sum(x[i]*(inputWeights.T)[j])
        # 将计算隐藏层节点的值经过sigmoid函数转换一下
        hidden_values = sigmoid(hidden_values - gamaBias)
        for j in range(outputNum):
            # 计算输出预测的y值
            predict_y[i][j] = np.sum(hidden_values*(outputWeights.T)[j])
            # 将输出结果经过sigmoid函数
        predict_y[i] = sigmoid(predict_y[i] - thetaBias)
    return predict_y



def backPropagation(x,y,hidden_layers_num = 5,epsilon_error = 0.1,learning_rate=0.1,rate = 1):
    '''
    构造一个三层的全连接神经网络，实现简单的bp算法
    :param x: 输入x(ndarray)
    :param y: 输出实际的y(ndarray)
    :param hidden_layers_num:隐藏层节点数
    :param epsilon_error:误差阈值
    :param learning_rate: 学习率
    :param rate: 算法结束时，达到误差阈值的样本占总体的最小比例
    :return: 训练好的各个参数
    '''
    # 样本总数
    dataNum = x.shape[0]
    # 输入层节点数
    inputNum = x.shape[1]
    # 输出层节点数
    outputNum = y.shape[1]
    # 随机初始化输入层到隐藏层的权重矩阵
    inputWeights = np.random.rand(inputNum,hidden_layers_num)
    # 随机初始化隐藏层到输出层的权重矩阵
    outputWeights = np.random.rand(hidden_layers_num,outputNum)
    # 隐含层 bias
    gamaBias = np.random.random(hidden_layers_num)
    # 输出层bias
    thetaBias = np.random.random(outputNum)
    # 初始化误差
    errors = 10
    # index 确保每个样本预测值与真实值的误差均小于设定的阈值
    index = 0
    while(errors > epsilon_error and index < dataNum*rate):
        index = 0
        for i in range(dataNum):
            # 初始化隐藏层节点的值
            hidden_values = np.zeros(hidden_layers_num)
            for j in range(hidden_layers_num):
                hidden_values[j] = np.sum(x[i]*(inputWeights.T)[j])
            # 将计算隐藏层节点的值经过sigmoid函数转换一下
            hidden_values = sigmoid(hidden_values - gamaBias)
            # 初始化输出y的值
            predict_y = np.zeros(outputNum)
            for j in range(outputNum):
                # 计算输出预测的y值
                predict_y[j] = np.sum(hidden_values*(outputWeights.T)[j])
            # 将输出结果经过sigmoid函数
            predict_y = sigmoid(predict_y - thetaBias)
            # 计算均方误差
            errors = mse(y[i],predict_y)
            print("errors:%.4f" % errors)
            if(errors > epsilon_error):
                # 计算参数g
                g = predict_y*(1-predict_y)*(y[i]-predict_y)
                # 初始化参数e
                e = np.zeros(hidden_layers_num)
                for j in range(hidden_layers_num):
                    e[j] = hidden_values[j]*(1-hidden_values[j])*(np.sum(outputWeights[j]*g))
                # 更新 outputWeights
                for j in range(hidden_layers_num):
                    outputWeights[j] += learning_rate*hidden_values[j]*g
                # 更新 thetaBias
                thetaBias += -learning_rate*g
                # 更新 inputWeights
                for j in range(inputNum):
                    inputWeights[j] += learning_rate*x[i][j]*e
                # 更新 gamaBias
                gamaBias += -learning_rate*e
            else:
                 index += 1

    return (gamaBias,inputWeights,thetaBias,outputWeights)


if __name__ == '__main__':
    # 样本数量
    dataNum = 100
    x = np.random.random((dataNum,2))
    y = np.zeros((dataNum,1))
    for i in range(dataNum):
        y[i][0] = np.exp(x[i][0] + x[i][1]) + x[i][0]*x[i][1] + 0.02*np.random.random()-0.01
    y_max = np.max(y)
    # 将 y 标准化，映射到[0,1]
    y_norm = y/(y_max)
    epsilon_error = 0.005
    learning_rate = 0.1
    rate = 1
    outputNum = 1
    # 隐藏层节点数目
    hidden_layers_num = 20
    gamaBias,inputWeights,thetaBias,outputWeights = backPropagation(x,y_norm,hidden_layers_num=hidden_layers_num,
                                                                    epsilon_error=epsilon_error,learning_rate=learning_rate,rate=rate)
    # 测试数据数量
    test_size = 20
    # 测试数据
    x_test = np.random.random((test_size,2))
    # 测试数据实际y值
    y_test = np.zeros((test_size,1))
    for i in range(test_size):
        y_test[i][0] = np.exp(x_test[i][0] + x_test[i][1]) + x_test[i][0]*x[i][1]
    # 预测值
    predict_y_test = calculate(x_test,outputNum=outputNum,hidden_layers_num=hidden_layers_num,
                          inputWeights=inputWeights,outputWeights=outputWeights,gamaBias=gamaBias,
                          thetaBias=thetaBias)
    # 将predict_y_test 从[0,1]映射回去
    predict_y_test *= y_max
    print("y_test:",y_test)
    print("predict_y_test:",predict_y_test)


