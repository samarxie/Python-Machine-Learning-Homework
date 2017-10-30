# -*- coding:utf-8 -*-
'''
@author:lyrichu
@email:919987476@qq.com
@description:求两个字符串的最大公共子序列(LCS)的长度(使用动态规划)。
参考博文:http://www.cnblogs.com/hapjin/p/5572483.html
'''

def solve_lcs(str1,str2):
	'''
	求解 LCS
	:param str1:字符串1
	:param str2:字符串2
	:return: length of LCS
	'''
	len1,len2 = len(str1),len(str2)
	# arr[i][j] 表示的是字符串1长度为i，字符串2长度为j时的LCS的长度
	arr = [[0]*(len2+1) for _ in range(len1+1)]
	arr_lcs = [[[] for _ in range(len2+1)] for _ in range(len1+1)]
	for i in range(len1+1):
		for j in range(len2+1):
			if(i == 0 or j == 0):
				arr[i][j] = 0
				arr_lcs[i][j].append("")
			elif(str1[i-1] == str2[j-1]):
				arr[i][j] = arr[i-1][j-1] + 1
				arr_lcs[i][j] = [str+str1[i-1] for str in arr_lcs[i-1][j-1]]
			else:
				arr[i][j] = max(arr[i][j-1],arr[i-1][j])
				if(arr[i][j-1] > arr[i-1][j]):
					arr_lcs[i][j] = arr_lcs[i][j-1]
				elif(arr[i][j-1] < arr[i-1][j]):
					arr_lcs[i][j] = arr_lcs[i-1][j]
				else:
					arr_lcs[i][j] = [s for s in arr_lcs[i-1][j]]
					arr_lcs[i][j].extend(arr_lcs[i][j-1])
					# remove the repeat the lcs string
					arr_lcs[i][j] = list(set(arr_lcs[i][j]))
	print("All the lcs string of {} and {} is: {}".format(str1,str2,arr_lcs[len1][len2]))
	return arr[len1][len2]
	

	
if __name__ == '__main__':
	print("Please input the first string:")
	str1 = input()
	print("Please input the second string:")
	str2 = input()
	print("The LCS length of {0} and {1} is {2}.".format(str1,str2,solve_lcs(str1,str2)))
	