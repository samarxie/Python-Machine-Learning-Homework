# -*- coding:utf-8 -*-
'''
Python-Machine-Learning-Homework 文件索引
'''
import os
import re


class Search(object):
    def __init__(self,keyword,use_re = False):
        # 搜索的关键字
        self.keyword = keyword
        # 是否使用正则表达式
        self.use_re = use_re

    def search(self,dir = "."):
        search_list = [] # 搜索结果列表
        curdirs = os.listdir(dir) # 当前目录所有文件夹
        for curdir in curdirs:
            if re.match(r"^\d+$",curdir): # 如果是有效文件夹
                abs_dir_path = os.path.join(".",curdir) # 当前文件夹
                for file in os.listdir(abs_dir_path): # 列出文件夹下的所有文件
                    file_path = os.path.join(abs_dir_path,file) # 文件路径
                    if os.path.isfile(file_path): # 如果是文件
                        try:
                            with open(file_path,"r",encoding="utf-8") as f:
                                text = f.read()
                        except UnicodeDecodeError:
                            continue
                        if self.use_re: # 使用正则表达式
                            if re.search(self.keyword,text):
                                search_list.append(file_path)
                        else: # 普通搜索
                            if self.keyword in text:
                                search_list.append(file_path)
                    else:
                        continue
        return search_list




if __name__ == '__main__':
    keyword = input("Please input your search keyword:")
    res = input("Do you want to use regular expression?\n"
                   "0 for True and 1 for False")
    if res == "0":
        use_re = True
    else:
        use_re = False
    s = Search(keyword,use_re)
    search_list = s.search()
    if search_list:
        print("%d files match your keyword '%s':" %(len(search_list),keyword))
        for index,file in enumerate(search_list,1):
            print("%d: %s" %(index,file))

    else: # 没有找到任何结果
        print("Sorry!Can't search anything about '%s'!" % keyword)





