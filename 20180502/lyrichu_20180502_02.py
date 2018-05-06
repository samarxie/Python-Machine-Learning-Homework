# -*- coding:utf-8 -*-
'''
Q2:给定一个严格递增数组arr和一个数字target,arr中的数字都是正数且唯一，
target为正整数,求出arr中和为target的所有数字组合,数字可以重复使用，返回所有可能的组合.
比如arr=[1,2,3,5,7],target = 5,返回[[1,1,1,1,1],[1,1,1,2],[1,2,2],[1,1,3],[2,3],[5]]
'''
def solution(arr,target):
	'''
	@param arr:原数组(已经是递增排序的)
	@param target:目标和
	'''
	result = [] # 存放最后结果
	tmp = [] # 存放中间结果
	dfs(arr,target,0,tmp,result)
	return result

def dfs(arr,target,index,tmp,result):
	'''
	@param arr:原数组
	@param target:目标和
	@param index:当前搜索位置
	@return:None
	'''
	if target == 0: # 找到一个可行解
		result.append(tmp.copy()) #注意一定要复制拷贝!!!
		return
	for i in range(index,len(arr)):
		if target < arr[i]: # 解已经不合法
			return 
		tmp.append(arr[i]) # 添加新的数字
		dfs(arr,target-arr[i],i,tmp,result)
		# 撤回一步(回溯)
		tmp.pop() 

if __name__ == '__main__':
	target = int(input()) # 目标和
	arr = sorted(map(int,input().split()))
	result = solution(arr,target)
	# 打印结果
	for v in result:
		for i in v:
			print(i,end = " ")
		print("")





