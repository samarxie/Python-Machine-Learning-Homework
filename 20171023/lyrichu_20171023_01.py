# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:
Q1:小明新买了一本算法书，算法书一共有n页，页码从1到n。在这本算法书页码中0~9每个数字分别出现了多少次？ 
输入描述:
输入包括一个整数n(1 ≤ n ≤ 1,000,000,000)
输出描述:
输出包括一行10个整数，即0~9这些数字在页码中出现的次数，以空格分隔。行末无空格。
示例1
输入
999
输出
189 300 300 300 300 300 300 300 300 300
'''
from collections import Counter

def count_nbers_by_counter(n):
	'''
	统计1-n中，数字0-9出现的次数(直接使用python内置计数器,效率一般)
	:param n: 正整数 n
	:return: 数字0-9出现次数
	'''
	counter = Counter()
	for i in range(1,n+1):
		counter.update(map(int,str(i)))
	# counts 是 0-9 每个数字出现次数列表
	counts = [counter[i] for i in range(10)]
	return counts
	
def count_nbers_by_digits(n):
	'''
	逐位求解
	:param n: 正整数 n
	:return: 数字0-9出现次数列表
	'''
	counts = [0]*10 
	digit = 1  # 个位
	while(True):
		low = n % digit
		cur = int((n % (10 * digit)) / digit)
		high = int(n / (10 * digit))  # 将数字分割, 例如 digit为100时, 表示百位. 12345 将有 high = 12, cur = 3, low = 45
		if cur == 0 and high == 0:
			break
		for i in range(10):  # 从0到9, 计算i在digit位出现的次数.
			if i < cur:
				if i == 0:  # 这里主要是因为 0 不能作为数字的开头.
					counts[i] += high * digit
				else:
					counts[i] += (high+1) * digit
			elif i == cur:
				if i==0:
					counts[i] += (high-1) * digit + low + 1
				else:
					counts[i] += high * digit + low + 1
			else:
				if i == 0:
					counts[i] += (high-1) * digit
				else:
					counts[i] += high * digit
		digit *= 10  # 下一位
	return counts

if __name__ == '__main__':
	n = int(input())
	counts_by_digits = count_nbers_by_digits(n)
	print(" ".join(map(str,counts_by_digits)))
	counts_by_counter = count_nbers_by_counter(n)
	print(" ".join(map(str,counts_by_counter)))
	