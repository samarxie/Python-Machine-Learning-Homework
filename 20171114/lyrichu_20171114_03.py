# -*- coding:utf-8 -*-
'''
Q3:实现散列表开放寻址法中的线性探查，二次探查以及双重散列。
还是以搜索字符串为例。
'''
import random
import sys 
import os
import time

class Hash():
	def __init__(self,hash_size=2**15):
		self.hash_size = hash_size
		self.hash_table = [0]*hash_size
		
	# 随机产生长度在min_len 到 max_len 之间的字符串
	def random_str(self,min_len=1,max_len=8):
		str = ""
		# r 在 1-8之间
		r = random.randrange(1,9)
		a = ord('a') # 97
		z = ord('z') # 122
		for _ in range(r):
			str += chr(random.randrange(a,z+1))
		return str 
		
	
	def write_str_to_file(self,filename,mode = "a",num=10000,min_len=1,max_len=8):
		'''
		随机写入字符串到文件
		:param filename: 文件名
		:param mode: 读写方式
		:param num: 写入字符串个数
		:param min_len:随机字符串最短长度
		:param max_len:随机字符串最长长度
		:return: None
		'''
		with open(filename,mode) as f:
			for _ in range(num):
				f.writelines(self.random_str(min_len,max_len)+'\n')
	
	def file_str_to_hashtable(self,filename,method=3):
		'''
		从文件读取字符串插入hash表
		:param filename: 文件名
		:param method:采用的hash函数
		:return:None
		'''
		with open(filename,"r") as f:
			index = 1
			for line in f:
				if index % 10000 == 0:
					print("line ",index)
				# 去除空白换行符等
				line = line.strip()
				self.hash_insert(line,method)
				index += 1
	def get_lines_num(self,filename):
		'''
		返回文件行数
		'''
		with open(filename,"r") as f:
			return len(f.readlines())
	
	
	def str_to_int(self,str,m=5):
		'''
		将字符串转为整数
		:param str: 字符串
		:param m:基数
		'''
		length = len(str)
		sum = 0
		for i in range(length):
			sum += (ord(str[i])-ord('a')+1)*(m**(length-1-i))
		return sum
		
	def mul_hash(self,str,m=5,p=15,A=0.618):
		'''
		使用乘法散列法计算散列值
		:param str: 字符串
		:param m: 基数
		:param p: 哈希表长度m=2**p 
		:param A: 0<A<1,h(k) = [m(kA mod 1)],[] 表示取整
		:return: 散列(哈希)值
		'''
		# 字符串到整数
		number = self.str_to_int(str,m)
		m = 2**p;
		return int(m*(number*A-int(number*A)))
		
	def div_hash(self,str,m=5):
		'''
		使用除法散列法计算散列值,并保证返回值一定为奇数
		:param m:基数
		:return: 奇数hash值
		'''
		# 字符串到整数
		number = self.str_to_int(str,m)
		hash = number % self.hash_size
		return hash if hash % 2 == 1 else hash+1
		
		
	def linear_hash(self,h,i):
		'''
		线性探查
		:param i: 第 i个位置
		:param h: 辅助散列值
		:return: 线性探查得到的散列(哈希)值
		'''
		return (h+i) % self.hash_size
		
	def quadratic_hash(self,h,i,c1=3,c2=5):
		'''
		二次探查 ,h(k,i) = (h(k)+c1*i+c2*i**2) mod m
		:param i: 第 i个位置
		:param c1: 二次探查参数1
		:param c2: 二次探查参数2
		:param h: 辅助散列值
		:return: 二次探查得到的散列(哈希)值
		'''
		return (h + c1*i + c2*i**2) % self.hash_size
		
	def double_hash(self,h1,h2,i):
		'''
		双重散列
		:param h1:第一个hash 值
		:param h2:第二个hash值
		:param i: 位置 i 
		:return: 双重散列值
		'''
		return (h1 + i*h2) % self.hash_size
		
	def hash_insert(self,str,method=3):
		'''
		hash 表插入 
		:param str: 字符串
		:param method: 选择的方法,1：线性探查 2:二次探查 3：双重散列
		'''
		i = 0
		if method == 1 or method == 2:
			if method == 1:
				hash_func = self.linear_hash
			else:
				hash_func = self.quadratic_hash
			h = self.mul_hash(str)
			while i < self.hash_size:
				j = hash_func(h,i)
				if self.hash_table[j] == 0:
					self.hash_table[j] = [str,1] # 第二个表示出现次数
					# 返回插入的位置
					return j
				# 如果碰到了相同的字符串
				elif self.hash_table[j][0] == str:
					# 字符串出现次数加1
					self.hash_table[j][1] += 1
					return j 
				else:
					i += 1
		else:
			h1 = self.mul_hash(str)
			h2 = self.div_hash(str)
			while i <self.hash_size:
				j = self.double_hash(h1,h2,i)
				if self.hash_table[j] == 0:
					self.hash_table[j] = [str,1] # 第二个表示出现次数
					# 返回插入的位置
					return j
				# 如果碰到了相同的字符串
				elif self.hash_table[j][0] == str:
					# 字符串出现次数加1
					self.hash_table[j][1] += 1
					return j 
				else:
					i += 1
		print("Hash table overflow!\n")
		return -1		
			
	def hash_search(self,str,method=3):
		'''
		hash表搜索
		:param str: 待搜索的字符串
		:return: 字符串出现次数 
		'''
		i = 0
		if method == 1 or method == 2:
			if method == 1:
				hash_func = self.linear_hash
			else:
				hash_func = self.quadratic_hash
			h = self.mul_hash(str)
			while i < self.hash_size:
				j = hash_func(h,i)
				if self.hash_table[j] == 0:
					return 0
				# 找到字符串
				elif self.hash_table[j][0] == str:
					# 返回出现次数
					return self.hash_table[j][1]
				else:
					i += 1
		else:
			h1 = self.mul_hash(str)
			h2 = self.div_hash(str)
			while i < self.hash_size:
				j = self.double_hash(h1,h2,i)
				if self.hash_table[j] == 0:
					return 0
				# 找到字符串
				elif self.hash_table[j][0] == str:
					# 返回出现次数
					return self.hash_table[j][1]
				else:
					i += 1
		return 0
		
	

		
					
		
			
		
		
	
# 测试函数
class Test():
	def __init__(self):
		self.obj = Hash()
	
	def str_to_int_test(self):
		assert(self.obj.str_to_int("abc") == (3+2*5+5**2))
		assert(self.obj.str_to_int("z") == 26)
		assert(self.obj.str_to_int("zxy",4) == 25 + 24*4 + 26*4**2)
	
	def mul_hash_test(self):
		assert(self.obj.mul_hash("abc") == 15859)
		assert(self.obj.mul_hash("d") == 15466)
		assert(self.obj.mul_hash("zy",4,20,0.7) == 314572)
		
	def hash_search_test(self):
		filename = "random_str.txt"
		# 文件绝对路径
		abs_filename = os.path.join(sys.path[0],filename)
		hash1 = Hash()
		hash1.file_str_to_hashtable(abs_filename,method=1)
		assert(hash1.hash_search("q",method=1) == 54)
		assert(hash1.hash_search("wco",method=1) == 1)
		assert(hash1.hash_search("wto",method=1) == 0)
		hash2 = Hash()
		hash2.file_str_to_hashtable(abs_filename,method=2)
		assert(hash2.hash_search("q",method=2) == 54)
		assert(hash2.hash_search("wco",method=2) == 1)
		assert(hash2.hash_search("wto",method=2) == 0)
		hash3 = Hash()
		hash3.file_str_to_hashtable(abs_filename)
		assert(hash3.hash_search("q") == 54)
		assert(hash3.hash_search("wco") == 1)
		assert(hash3.hash_search("wto") == 0)
		
	def get_lines_num_test(self):
		filename = os.path.join(sys.path[0],"str.txt")
		assert(self.obj.get_lines_num(filename) == 2000000)
		
		
		
	def run_all_tests(self):
		self.str_to_int_test()
		self.mul_hash_test()
		self.hash_search_test()
		
def print_str_nums(filename):
	# 文件绝对路径
	abs_filename = os.path.join(sys.path[0],filename)
	hash = Hash(2**21)
	lines = hash.get_lines_num(abs_filename) # 文件行数
	print("Please input the method you use:1--linear_hash,2--quadratic_hash,3--double_hash:")
	method = int(input())
	# hash 表初始化
	time_start = time.time()
	hash.file_str_to_hashtable(abs_filename,method)
	print("Init hash table of %d words costs %.3f seconds" %(lines,time.time()-time_start))
	while True:
		print("Please input the strings you want to search(only lower alphabets allowed,0 for exit):")
		str = input()
		while str != "0":
			time_start = time.time()
			count = hash.hash_search(str,method)
			time_end = time.time()
			print("Search costs %.3f seconds of all %d words" %(time_end-time_start,lines))
			print("%s ocuurs %d times in file %s" %(str,count,filename))
			str = input()
		
		
		
	
if __name__ == '__main__':
	#test = Test()
	#test.run_all_tests()
	filename = "str.txt"
	print_str_nums(filename)
	
	
	
	
	
	
