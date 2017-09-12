#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/9/11 12:53
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : lyrichu_20170911_02.py
'''
@Description:
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，形成一个数组如下： a, aa, aaa, aaaa, aaab,
aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy 其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，
输入是任意一个编码，输出这个编码对应的Index.


	输入描述:

	输入一个待编码的字符串,字符串长度小于等于100.



	输出描述:

	输出这个编码的index


	输入例子1:

	baca

	输出例子1:

	16331
'''

def getIndex(s):
    alphabet = [chr(i+97) for i in range(25)]
    alphabet.insert(0,'0')
    res_list = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for t in range(26):
                    string = alphabet[i] + alphabet[j]+alphabet[k]+alphabet[t]
                    string = string.replace('0','')
                    if(string is not ''):
                        res_list.append(string)
    res_list = list(set(res_list))
    res_list.sort()
    return res_list.index(s)



if __name__ == '__main__':
    print(getIndex(raw_input()))
