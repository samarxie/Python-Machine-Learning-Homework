#!/usr/bin/env python3.6
# encoding: utf-8
"""
@version: 0.1
@author: lyrichu
@license: Apache Licence 
@contact: 919987476@qq.com
@software: PyCharm
@file: lyrichu_20170915_04.py
@time: 2017/9/26 11:13
@description:
熟悉python的urllib2(python2.x)或urllib3(python3.x),具体可以参考博文:http://www.cnblogs.com/wly923/archive/2013/05/07/3057122.html
(urllib2) 和 http://www.cnblogs.com/KGoing/p/6146999.html(urllib3),或者阅读官方文档:https://docs.python.org/2/library/urllib2.html
,https://urllib3.readthedocs.io/en/latest/。
实现下面的功能。
(1)抓取http://news.sina.com.cn/o/2017-09-13/doc-ifykuftz6758652.shtml 的新闻内容。将其内容保存到news1.txt，并统计新闻总字数(不算标点符号)
，共出现多少个不同的字，以及每个字出现次数(不算标点)。
(2)抓取 http://slide.news.sina.com.cn/z/slide_1_64237_200066.html#p=1 的一组图片。将其保存到 images文件夹下，每张图片按照1.jpg,2.jpg,...
这样的格式命名。并且抓取每张图片下面的文字，将所有文字保存到comments.txt 文件。
"""
from __future__ import print_function
import urllib2
import re
import os
import codecs
from collections import Counter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 新闻url
url1 = "http://news.sina.com.cn/o/2017-09-13/doc-ifykuftz6758652.shtml"
# 图片的url
imgUrl = "http://slide.news.sina.com.cn/z/slide_1_64237_200066.html#p=1"

def getHtml(url):
    '''
    抓取url对应的html源码
    :param url: 传入url
    :return: html的content
    '''
    return urllib2.urlopen(url).read()


def getNews(html):
    '''
    :param html: 传入html
    :return: 抓取到的news(使用正则匹配)
    '''
    # 匹配模式
    pattern = r'<p>(.+)</p>'
    res = re.findall(pattern=pattern,string=html)
    # 返回news
    return ("".join(res[0:4]).decode("utf-8"))

def chooseChinese(String):
    '''
    将字符串中的空白符以及标点等删除，只保留字母以及汉字
    中文以及
    :param String:源字符串
    :return: 处理之后的字符串
    '''
    # 初始化结果字符串
    res = ''
    uMin = int('0x4E00',16) # 汉字unicode 编码的下界
    uMax = int('0x9FA5',16) # 汉字unicode编码的上界
    for s in String:
        # 获取所有的数字、字母以及中文汉字
        if((s >= '0' and s <= '9') or (s >= 'a' and s <= 'z') or (s >='A' and s <='Z')
           or (ord(s) >= uMin and ord(s) <= uMax)):
            res += s
    return res

def saveNews(newsPath,news):
    '''
    保存抓取到新闻内容
    :param newsPath: 保存新闻地址
    :param news:新闻内容
    :return: None
    '''
    with codecs.open(newsPath,'w',encoding='utf-8') as f:
        f.write(news)


def saveImages(savePath):
    '''
    保存图片到本地
    :param savePath: 保存图片的路径
    :return: None
    '''
    # 初始化当前图片索引
    index = 1
    # 如果文件夹不存在，则创建
    while(not os.path.exists(savePath)):
        os.mkdir(savePath)
    html = getHtml(imgUrl)
    # 匹配图片的pattern
    pattern = r'(http://n.sinaimg.cn/news/1_img/upload.+jpg)'
    # 图片url列表
    imgDownloadUrlList = re.findall(pattern,html)
    # 逐个保存
    for imgDownloadUrl in imgDownloadUrlList:
        # 读取图片二进制
        img = getHtml(imgDownloadUrl)
        # 图片保存地址
        imgPath = savePath + "%d.jpg" % index
        with open(imgPath,'wb') as f:
            f.write(img)
        print("成功写入第%d张图片" % index)
        index += 1

def saveComments(commentsName):
    '''
    保存图片下方的评论
    :param commentsName:保存文件名字
    :return:None
    '''
    html = getHtml(imgUrl)
    pattern = r'<p>(.+)</p>'
    commentsList = re.findall(pattern,html)
    # 提取有效信息
    commentsList = commentsList[-19:]
    # 将评论写入文件
    with open(commentsName,'w') as f:
        for comments in commentsList:
            # 注意编码转换
            f.writelines(comments.decode('gbk').encode('utf-8')+'\n')









if __name__ == '__main__':
    html = getHtml(url1)
    res = getNews(html)
    # 去除标点符号等
    res = chooseChinese(res)
    print("新闻总字数:%d" % len(res))
    print("新闻共出现%d个不同的字:" % len(set(res)))
    print("每个不同字出现次数(按照(字:次数)的格式):")
    for pair in Counter(res).most_common():
        print("%s:%d" %(pair[0],pair[1]))
    # 保存新闻到 news1.txt
    newsPath = 'news1.txt'
    saveNews(newsPath,res)
    # 保存图片路径
    saveImgPath = "images/"
    saveImages(savePath=saveImgPath)
    # 评论文件名
    commentsName = 'comments.txt'
    # 保存评论到文件
    saveComments(commentsName)






















