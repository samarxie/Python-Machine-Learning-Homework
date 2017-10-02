#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170930_01.py
@time: 2017/10/1 16:54
@description:设计一个程序，使得该程序的输出就是该程序本身。
"""
import os

def printItself():
    with open(__file__,'r') as f:
        print(f.read())

if __name__ == '__main__':
    printItself()
